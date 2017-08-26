#!/usr/bin/env python3

import argparse

import lib.jnlib

"""
Make shell files from jupyter notebook files.
usage: make_shell_from_notebook.py [-h] [dir_path]
"""

parser = argparse.ArgumentParser(
    description='Make shell files from jupyter notebook files.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')

args = parser.parse_args()
lib.jnlib.make_simple_shell(args.dir_path)
