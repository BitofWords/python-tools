#!/usr/bin/env python3

import os
import argparse

import lib.filelib

parser = argparse.ArgumentParser(
    description='Add suffix.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('suffix', help='strings of suffix')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

suffix = args.suffix
dir_path = args.dir_path
if args.ext[0] == '.':
    ext = args.ext[1:]
else:
    ext = args.ext

files = lib.filelib.get_file_list(dir_path, ext, True)

for f in files:
    root, ext = os.path.splitext(f)
    new_path = root + suffix + ext
    os.rename(f, new_path)
    print("{} > {}".format(f, new_path))
