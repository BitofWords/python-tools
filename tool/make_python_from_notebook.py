#!/usr/bin/env python3

import argparse

import lib.jn_util

"""
Make python files from jupyter notebook files.
usage: make_python_from_notebook.py [-h] [dir_path]
"""

parser = argparse.ArgumentParser(
    description='Make python files from jupyter notebook files.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')

args = parser.parse_args()
lib.jn_util.make_simple_python(args.dir_path)
