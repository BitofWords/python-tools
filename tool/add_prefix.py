#!/usr/bin/env python3

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
ext = args.ext

lib.filelib.add_prefix_batch(prefix, dir_path, ext)
