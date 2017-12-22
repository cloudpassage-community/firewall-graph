import cloudpassage
import os
from firewallgraph import FirewallGraph


def main():
    halo_key = os.getenv('HALO_API_KEY')
    halo_secret = os.getenv('HALO_API_SECRET_KEY')
    target = os.getenv('TARGET')
    session = cloudpassage.HaloSession(halo_key, halo_secret)
    try:
        result = generate_group_firewall_report(session, target)
        print(result)
    except Exception as e:
        print("Exception caught!\n %s" % e)
    return


def get_id_for_group_target(session, target):
    """Attempts to get group_id using arg:target as group_name, then id"""
    group = cloudpassage.ServerGroup(session)
    orig_result = group.list_all()
    result = []
    for x in orig_result:
        if x["name"] == target:
            result.append(x)
    if len(result) > 0:
        return result[0]["id"]
    else:
        try:
            result = group.describe(target)["id"]
        except cloudpassage.CloudPassageResourceExistence:
            result = None
        except KeyError:
            result = None
    return result


def generate_group_firewall_report(session, target):
    group_id = get_id_for_group_target(session, target)
    if group_id is None:
        retval = "Group not found: %s\n" % target
    else:
        retval = firewall_report_for_group_id(session, group_id)
    return retval


def firewall_report_for_group_id(session, group_id):
    fw_obj = cloudpassage.FirewallPolicy(session)
    group_obj = cloudpassage.ServerGroup(session)
    group_struct = group_obj.describe(group_id)
    fw_polid = group_struct["linux_firewall_policy_id"]
    if fw_polid is None:
        retval = "No firewall policy for: %s\n" % group_id
    else:
        grapher = FirewallGraph(fw_obj.describe(fw_polid))
        retval = FirewallGraph.dot_to_png(grapher.make_dotfile())
    return retval


if __name__ == '__main__':
    main()
