#!/usr/bin/env python3

import argparse

import lib.filelib

"""
Add suffix to filename of files at the directory with the extension.
usage: python add_suffix.py [-h] suffix [dir_path] [ext]
"""

parser = argparse.ArgumentParser(
    description='Add suffix.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('suffix', help='strings of suffix')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

lib.filelib.add_prefix_suffix_batch('', args.suffix, args.dir_path,
                                    args.ext, False)
