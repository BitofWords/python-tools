#!/usr/bin/env python3

import argparse

import lib.filelib

"""
Remove head of filename of files at the directory with the extension.
usage: python remove_head_of_filename.py [-h] num [dir_path] [ext]
"""

parser = argparse.ArgumentParser(
    description='Remove head of filename.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('num', help='number of strings to remove', type=int)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')
parser.add_argument('ext', help='extension', nargs='?', default='*')

args = parser.parse_args()

remove_num = args.num
dir_path = args.dir_path
ext = args.ext

lib.filelib.remove_head_tail_batch(remove_num, 0, dir_path, ext)
