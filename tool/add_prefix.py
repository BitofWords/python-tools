#!/usr/bin/env python3

import os
import argparse

import lib.filelib

parser = argparse.ArgumentParser(
    description='Add prefix.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('prefix', help='strings of prefix')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

prefix = args.prefix
dir_path = args.dir_path
if args.ext[0] == '.':
    ext = args.ext[1:]
else:
    ext = args.ext

files = lib.filelib.get_file_list(dir_path, ext, True)

for f in files:
    new_path = os.path.join(dir_path, prefix + os.path.basename(f)) 
    os.rename(f, new_path)
    print("{} > {}".format(f, new_path))
