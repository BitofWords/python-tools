#!/usr/bin/env python3

import os
import argparse

import lib.filelib

parser = argparse.ArgumentParser(
    description='Replace strings at filename.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('old_str', help='old strings')
parser.add_argument('new_str', help='new strings')
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

old = args.old_str
new = args.new_str
dir_path = args.dir_path
ext = args.ext

files = lib.filelib.get_file_list(dir_path, ext, True)

change_list = []

for f in files:
    if old in f:
        new_path = os.path.join(dir_path, os.path.basename(f).replace(old, new))
        change_list.append([f, new_path])
        print("{} > {}".format(f, new_path))

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
