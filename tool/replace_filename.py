#!/usr/bin/env python3

import argparse

import lib.filelib

"""
Replace filename of files at the directory with the extension.
usage: replace_filename.py [-h] old_str new_str [dir_path] [ext]
"""

parser = argparse.ArgumentParser(
    description='Replace strings at filename.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('old_str', help='old strings')
parser.add_argument('new_str', help='new strings')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

lib.filelib.replace_filename_batch(args.old_str, args.new_str,
                                   args.dir_path, args.ext)
