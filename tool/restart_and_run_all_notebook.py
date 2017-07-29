#!/usr/bin/env python3

import argparse

import lib.jn_util

"""
Restart and run all jupyter notebook files.
usage: restart_and_run_all_notebook.py [-h] [dir_path]
"""

parser = argparse.ArgumentParser(
    description='Restart and run all jupyter notebook files.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')

args = parser.parse_args()
lib.jn_util.restart_and_run_all(args.dir_path)
