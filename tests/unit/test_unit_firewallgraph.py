import imp
import os
import sys

module_name = 'firewallgraph'
here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)
firewallgraph = imp.load_module(module_name, fp, pathname, description)

# V1 policy, as would be accepted by the API
policy_json = {"firewall_policy":
               {"name": "Policy_Name",
                "description": "AUTOMATED TEST",
                "platform": "linux",
                "ignore_forwarding_rules": True,
                "firewall_rules": [
                  {
                    "chain": "INPUT",
                    "active": True,
                    "firewall_interface": None,
                    "firewall_source": {
                      "name": "All GhostPorts users",
                      "type": "UserGroup"
                    },
                    "firewall_service": None,
                    "connection_states": "NEW, ESTABLISHED",
                    "action": "ACCEPT",
                    "log": False
                  },
                  {
                    "chain": "INPUT",
                    "active": True,
                    "firewall_interface": None,
                    "firewall_source": {
                      "name": "All Active Servers",
                      "type": "Group"
                    },
                    "firewall_service": None,
                    "connection_states": "NEW, ESTABLISHED",
                    "action": "ACCEPT",
                    "log": False
                  },
                  {
                    "chain": "INPUT",
                    "active": True,
                    "firewall_interface": None,
                    "firewall_source": None,
                    "firewall_service": None,
                    "connection_states": None,
                    "action": "REJECT",
                    "log": True,
                    "comment": "Default reject-all"
                  },
                  {
                    "chain": "OUTPUT",
                    "active": True,
                    "firewall_interface": None,
                    "firewall_target": None,
                    "firewall_service": None,
                    "connection_states": None,
                    "action": "ACCEPT",
                    "log": False
                  }
                ]}}

# Dumped out from API V2
policy_json_2 = {"firewall_policy":
                 {"id": "6d7",
                  "url": "https://portal.cloudpassage.com",
                  "name": "AMI", "module": "fw", "created_by": None,
                  "updated_by": None, "created_at": "2014-01-14T22:23:34.057Z",
                  "updated_at": "2016-04-26T12:51:40.987Z",
                  "group_id": "4d61bff",
                  "group_name": "Cloud Passage",
                  "description": "General AMI policy.",
                  "platform": "linux", "shared": True, "read_only": False,
                  "used_by": [{"id": "7a",
                               "name": "LIDS-Health"}],
                  "firewall_rules": [{"id": "r1234",
                                      "url": "https://portal.cloudpassage.com",
                                      "chain": "INPUT", "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None, "log": False,
                                      "log_prefix": None, "comment": None,
                                      "firewall_source": {"id": "r1234",
                                                          "url": "https://po",
                                                          "name": "NewOffice",
                                                          "group_id": "r1234",
                                                          "group_name": "Cloud Passage",
                                                          "description": "",
                                                          "ip_address": "4.4.4.4",
                                                          "system": False,
                                                          "shared": True,
                                                          "type": "FirewallZone"}},
                                     {"id": "r1234",
                                      "url": "https://portal.cloudpassage.com/",
                                      "chain": "INPUT", "action": "ACCEPT",
                                      "active": True, "connection_states": None,
                                      "log": False, "log_prefix": None,
                                      "comment": "",
                                      "firewall_service": {"id": "r1234",
                                                           "url": "https://po",
                                                           "name": "ssh",
                                                           "group_id": None,
                                                           "group_name": None,
                                                           "protocol": "TCP",
                                                           "port": "22",
                                                           "system": True,
                                                           "shared": True},
                                      "firewall_source": {"id": "2663",
                                                          "url": "https://por",
                                                          "name": "Office",
                                                          "group_id": "4d61",
                                                          "group_name": "Cloud Passage",
                                                          "description": "Office on Townsend",
                                                          "ip_address": "4.4.4.4/32",
                                                          "system": False,
                                                          "shared": True,
                                                          "type": "FirewallZone"}},
                                     {"id": "8e33",
                                      "url": "https://portal",
                                      "chain": "INPUT",
                                      "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": "",
                                      "firewall_source": {"type": "UserGroup",
                                                          "name": "All GhostPorts users"}},
                                     {"id": "6dd7",
                                      "url": "https://portal",
                                      "chain": "INPUT",
                                      "action": "DROP",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": ""},
                                     {"id": "6dda",
                                      "url": "https://portal7",
                                      "chain": "OUTPUT",
                                      "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": "",
                                      "firewall_service": {"id": "ea3f",
                                                           "url": "https://p",
                                                           "name": "ssh",
                                                           "group_id": None,
                                                           "group_name": None,
                                                           "protocol": "TCP",
                                                           "port": "22",
                                                           "system": True,
                                                           "shared": True}},
                                     {"id": "6ddb",
                                      "url": "https://portal",
                                      "chain": "OUTPUT",
                                      "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": "",
                                      "firewall_service": {"id": "ea4b",
                                                           "url": "https://po",
                                                           "name": "http",
                                                           "group_id": None,
                                                           "group_name": None,
                                                           "protocol": "TCP",
                                                           "port": "80",
                                                           "system": True,
                                                           "shared": True}},
                                     {"id": "6de1",
                                      "url": "https://portal",
                                      "chain": "OUTPUT",
                                      "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": "",
                                      "firewall_service": {"id": "ea4b8",
                                                           "url": "https://po",
                                                           "name": "https",
                                                           "group_id": None,
                                                           "group_name": None,
                                                           "protocol": "TCP",
                                                           "port": "443",
                                                           "system": True,
                                                           "shared": True}},
                                     {"id": "6de6",
                                      "url": "https://portal",
                                      "chain": "OUTPUT",
                                      "action": "ACCEPT",
                                      "active": True,
                                      "connection_states": None,
                                      "log": False,
                                      "log_prefix": None,
                                      "comment": ""}],
                        "ignore_forwarding_rules": False}}


class TestUnitFirewallGraph:
    def test_unit_firewallgraph_instantiate(self):
        assert firewallgraph.FirewallGraph([])

    def test_unit_firewallgraph_make_dotfile(self):
        policy_content = policy_json["firewall_policy"]
        grapher = firewallgraph.FirewallGraph(policy_content)
        result = grapher.make_dotfile()
        print result
        assert isinstance(result, str)

    def test_unit_firewallgraph_make_dotfile_from_multi(self):
        policy_content = [policy_json["firewall_policy"],
                          policy_json_2["firewall_policy"]]
        grapher = firewallgraph.FirewallGraph(policy_content)
        result = grapher.make_dotfile()
        print result
        assert isinstance(result, str)

    def test_unit_normalize_firewall_rules(self):
        grapher = firewallgraph.FirewallGraph
        rules = policy_json["firewall_policy"]["firewall_rules"]
        result = grapher.normalize_fw_rules(rules, "test_name")
        assert isinstance(result, list)
        assert isinstance(result[0], tuple)

    def test_unit_parse_fw_policies(self):
        grapher = firewallgraph.FirewallGraph
        policy = policy_json["firewall_policy"]
        name = "Test Server"
        result = grapher.parse_fw_policies([policy])
        assert isinstance(result, list)
        assert isinstance(result[0], tuple)

    def test_unit_firewallgraph_dot_to_png(self):
        policy_content = policy_json["firewall_policy"]
        grapher = firewallgraph.FirewallGraph([policy_content])
        dotfile = grapher.make_dotfile()
        result = firewallgraph.FirewallGraph.dot_to_png(dotfile)
        print result
        assert isinstance(result, str)
