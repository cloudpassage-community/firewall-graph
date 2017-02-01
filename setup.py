import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    raw_init_file = read("firewallgraph/__init__.py")
    rx_compiled = re.compile(r"\s*__version__\s*=\s*\"(\S+)\"")
    ver = rx_compiled.search(raw_init_file).group(1)
    return ver


def get_long_description(fnames):
    retval = ""
    for fname in fnames:
        retval = retval + (read(fname)) + "\n\n"
    return retval


setup(
    name="firewallgraph",
    version=get_version(),
    author="CloudPassage",
    author_email="toolbox@cloudpassage.com",
    description="Turn CloudPassage Halo firewall policies into directed graphs",
    license="BSD",
    keywords="cloudpassage halo api firewall graph",
    url="http://github.com/halotools/firewall-graph",
    packages=["firewallgraph"],
    install_requires=["cloudpassage >= 1.0",
                      "networkx >= 1.11",
                      "pydot >= 1.2.3",
                      "pygraphviz >= 1.3.1"],
    long_description=get_long_description(["README.rst", "CHANGELOG.rst"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
        "License :: OSI Approved :: BSD License"
        ],
    )
