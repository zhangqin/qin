#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
from setuptools import setup, find_packages
setup(
    name="qin",
    version="1.0",
    description="b0lu's common packages and functions",
    author="b0lu",
    url="http://b0lu.xyz",
    license="LGPL",
    requires= ['smtplib'],
    packages= find_packages(),
)
