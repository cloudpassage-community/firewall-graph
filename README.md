# firewall-graph
##C reate a PNG file from a list of Halo firewall policies

Thanks a million to Jason Lancaster (@jasonblancaster) for the original work
that made it into this library.


## What it is
This is a Python library that accepts Halo Linux firewall policies and returns
.png files that show permitted traffic paths.

## How it works

    ```
    from firewallgraph import FirewallGraph

    firewall_policies = []  # This will be a list of Halo firewall policies
    generator = FirewallGraph(firewall_policies)
    dotfile_contents = generator.make_dotfile()
    b64_png = FirewallGraph.dot_to_png(dotfile_contents)

    ```

The `dot_to_png(dotfile_contents)` method returns a base64-encoded png file,
containing the rendered dotfile_contents.
