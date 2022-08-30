"""setup.py file."""
from setuptools import setup, find_packages
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "requirements.txt")) as f:
    requirements = f.read().split("\n")


__author__ = 'Shem Valentine <shem.valentine@vivint.com>'


setup(
    name="napalm-cumulus",
    version="4.0.3",
    packages=find_packages(exclude=["test", "test.*"]),
    author="Shem Valentine",
    author_email="shem.valentine@vivint.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://source.vivint.com/projects/POPS/repos/napalm-cumulus/browse",
    include_package_data=True,
    install_requires=requirements,
)
