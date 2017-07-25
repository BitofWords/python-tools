#!/usr/bin/env python3

import argparse

import lib.filelib

"""
Add prefix to filename of files at the directory with the extension.
usage: python add_prefix.py [-h] prefix [dir_path] [ext]
"""

parser = argparse.ArgumentParser(
    description='Add prefix.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('prefix', help='strings of prefix')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

lib.filelib.add_prefix_suffix_batch(args.prefix, '', args.dir_path,
                                    args.ext, False)
