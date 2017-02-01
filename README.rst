--------------
firewall-graph
--------------

Create a PNG file from a list of Halo firewall policies
=======================================================

Thanks a million to Jason Lancaster (@jasonblancaster) for the original work
that made it into this library.


What it is
==========

.. image:: https://travis-ci.org/cloudpassage-community/firewall-graph.svg?branch=master
   :target: https://travis-ci.org/cloudpassage-community/firewall-graph
.. image:: https://codeclimate.com/github/cloudpassage-community/firewall-graph/badges/gpa.svg
   :target: https://codeclimate.com/github/cloudpassage-community/firewall-graph
   :alt: Code Climate
.. image:: https://codeclimate.com/github/cloudpassage-community/firewall-graph/badges/coverage.svg
   :target: https://codeclimate.com/github/cloudpassage-community/firewall-graph/coverage
   :alt: Test Coverage
.. image:: https://codeclimate.com/github/cloudpassage-community/firewall-graph/badges/issue_count.svg
   :target: https://codeclimate.com/github/cloudpassage-community/firewall-graph
   :alt: Issue Count


This is a Python library that accepts Halo Linux firewall policies and returns
.png files that show permitted traffic paths.

Requirements
============

* Python 2.7
* Graphviz and associated development libraries (See the Dockerfile in this repo for details...)
* Other dependencies installed via setup routine:
    * cloudpassage >= 1.0
    * networkx >= 1.11
    * pydot >= 1.2.3
    * pygraphviz >= 1.3.1

How it works
============

::

    from firewallgraph import FirewallGraph

    firewall_policies = []  # This will be a list of Halo firewall policies
    generator = FirewallGraph(firewall_policies)
    dotfile_contents = generator.make_dotfile()
    b64_png = FirewallGraph.dot_to_png(dotfile_contents)



The `dot_to_png(dotfile_contents)` method returns a base64-encoded png file,
containing the rendered dotfile_contents.

Testing
=======

The easiest way to test is to try to build the Dockerfile:

::
    docker build .

If you want to test it natively, the testing dependencies (in addition to the
other dependencies, above) are:

* pytest
* pytest-flake8
* pytest-cov (for coverage metrics)
