import os
from setuptools import setup, find_packages
from typing import Any, Dict

# Get the version string. Cannot be done with import!
g: Dict[str, Any] = {}
with open(os.path.join("sword3common", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="sword3common",
    version=version,
    description="SWORDv3 Common Object Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    url="https://github.com/cottagelabs/sword3-common.py",
    author="Cottage Labs",
    author_email="richard@cottagelabs.com",
    license="Apache2",
    classifiers=[],
)
