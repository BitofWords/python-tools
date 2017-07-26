#!/usr/bin/env python3

import argparse
import lib.filelib
from unicodedata import normalize

parser = argparse.ArgumentParser(
    description='Display NFC normalized filename.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('dir_path', help='directory path', nargs='?', default='.')

args = parser.parse_args()

files = lib.filelib.get_file_list(args.dir_path, '*', False)

for f in files:
    print(normalize("NFC", f))
