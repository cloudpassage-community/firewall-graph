import networkx as nx
import tempfile
import shutil
import os
import pydot
import base64


class FirewallGraph(object):
    def __init__(self, firewall_policies):
        self.fw_policies = []
        self.set_firewall_policies(firewall_policies)
        self.norm_rules = FirewallGraph.parse_fw_policies(self.fw_policies)

    def set_firewall_policies(self, firewall_policies):
        """Make sure that even if it's one policy, it gets put into a list."""
        if isinstance(firewall_policies, list):
            self.fw_policies = firewall_policies
        else:
            self.fw_policies = [firewall_policies]
        return

    def make_dotfile(self):
        """Calling this method returns a text string in dot format.

        The dot-formatted text that is returned contains a directed graph of
        the firewall policies the object was originally instantiated with.

        """
        temp_path = tempfile.mkdtemp()
        rando = os.path.join(temp_path, "temporarius.dot")
        g = nx.DiGraph()
        g.add_edges_from(FirewallGraph.edge_generator(self.norm_rules))
        A = nx.drawing.nx_agraph.to_agraph(g)
        A.write(rando)
        with open(rando, 'r') as r_f:
            contents = r_f.read()
        shutil.rmtree(temp_path)
        return contents

    @classmethod
    def dot_to_png(cls, dotstring):
        """Turn the contents of a dotfile into a base-64 encoded png.
        Calling this class method with the contents of a dot-formatted file
        will get you a representation of the graph in png format,
        base64-encoded.

        """
        temp_path = tempfile.mkdtemp()
        outfile = os.path.join(temp_path, "outfile.png")
        (graph,) = pydot.graph_from_dot_data(dotstring)
        graph.write_png(outfile)
        with open(outfile, 'r') as pngfile:
            retval = pngfile.read()
        shutil.rmtree(temp_path)
        return base64.b64encode(retval)

    @classmethod
    def edge_generator(cls, rules):
        # edges = [(1,2),(1,3)]
        edges = []
        for rule in rules:
            edges.append((rule[0], rule[1]))
            edges.append((rule[1], rule[2]))
        return edges

    @classmethod
    def parse_fw_policies(cls, policies):
        results = []
        for policy in policies:
            rules = policy["firewall_rules"]
            name = policy["name"]
            results.extend(FirewallGraph.normalize_fw_rules(rules, name))
        return results

    @classmethod
    def normalize_fw_rules(cls, fw_rules, fw_name):
        results = []
        workload_name = "Workload:%s" % fw_name
        for fw_rule in fw_rules:
            # Only include fw rules that are active and permit traffic
            if (fw_rule['active'] is True and
                    fw_rule['action'] == 'ACCEPT' and
                    fw_rule['chain'] == "INPUT"):
                rule = ()
                if 'firewall_source' in fw_rule:
                    src_group = fw_rule['firewall_source']['name']
                else:
                    src_group = 'Everywhere'
                proto_port = FirewallGraph.dst_port_proto_from_rule(fw_rule)
                dst_tuple = ("%s:%s_%s" % (str(fw_name + "--INPUT"),
                                           proto_port[0], proto_port[1]))
                rule = (src_group, dst_tuple, workload_name)
                results.append(rule)
            elif (fw_rule['active'] is True and
                    fw_rule['action'] == 'ACCEPT' and
                    fw_rule['chain'] == "OUTPUT"):
                rule = ()
                if 'firewall_source' in fw_rule:
                    dst_group = fw_rule['firewall_source']['name']
                else:
                    dst_group = 'Everywhere'
                proto_port = FirewallGraph.dst_port_proto_from_rule(fw_rule)
                src_tuple = ("%s:%s_%s" % (str(fw_name + "--OUTPUT"),
                                           proto_port[0], proto_port[1]))
                rule = (workload_name, src_tuple, dst_group)
                results.append(rule)
        return results

    @classmethod
    def dst_port_proto_from_rule(cls, fw_rule):
        dst_protocol = 'Any'
        dst_port = 'Any'
        if ('firewall_service' in fw_rule and
           fw_rule['firewall_service'] is not None):
            if 'protocol' in fw_rule['firewall_service']:
                dst_protocol = fw_rule['firewall_service']['protocol']
            else:
                dst_protocol = 'Any'
            if 'port' in fw_rule['firewall_service']:
                dst_port = fw_rule['firewall_service']['port']
            else:
                dst_port = 'Any'
        return(dst_protocol, dst_port)
