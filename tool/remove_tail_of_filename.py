#!/usr/bin/env python3

import os
import argparse

import lib.filelib

parser = argparse.ArgumentParser(
    description='Remove tail of filename.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('num', help='number of strings to remove', type=int)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

remove_num = args.num
dir_path = args.dir_path
if args.ext[0] == '.':
    ext = args.ext[1:]
else:
    ext = args.ext

files = lib.filelib.get_file_list(dir_path, ext, True)

change_list = []

for f in files:
    base, ext = os.path.splitext(f)
    base = base[:-remove_num]
    change_list.append([f, base + ext])
    print("{} > {}".format(f, base + ext))

if len(change_list) == 0:
    print('no file')
else:
    answer = input("yes? ")
    if answer in ["y", "yes"]:
        for change in change_list:
            os.rename(change[0], change[1])
        print("done")
    else:
        print("skip")
