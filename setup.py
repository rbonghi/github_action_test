# Copyright (c) 2023 Raffaello Bonghi
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
project_homepage = "https://github.com/rbonghi/github_action_test"
documentation_homepage = "https://github.com/rbonghi/github_action_test"

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Load version package
with open(os.path.join(here, "foo", "__init__.py")) as fp:
    VERSION = (
        re.compile(r""".*__version__ = ["'](.*?)['"]""", re.S).match(fp.read()).group(1)
    )
# Store version package
version = VERSION


# Configuration setup module
setup(
    name="foo",
    version=version,
    author="Raffaello Bonghi",
    author_email="raffaello@rnext.it",
    description="Hello! I'm a repo to test github_actions",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=documentation_homepage,
    project_urls={
        'Documentation': documentation_homepage,
    },
    packages=find_packages(exclude=[]),  # Required
    keywords=("test"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Audience and topics
        "Intended Audience :: Developers",
        # License
        "License :: OSI Approved :: MIT",
        # Programming and Operative system
        "Programming Language :: Python :: 3.10",
        ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    platforms=["linux", "linux2", "darwin"],
    entry_points={'console_scripts': [
        'foo=foo.foo:hello',
    ]},
)
# EOF
