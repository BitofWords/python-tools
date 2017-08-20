#!/usr/bin/env python3

import argparse

from PIL import Image

import lib.imagelib

"""
Expand canvas of image to square.
usage: expand_canvas_square.py [-h] src_path dst_path dst_width [r] [g] [b]
"""

parser = argparse.ArgumentParser(
    description='Expand canvas to square.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('src_path', help='path of src image')
parser.add_argument('dst_path', help='path of dst image')
parser.add_argument('dst_width', type=int, help='width and height of dst image')
parser.add_argument('r', type=int, help='background red', nargs='?', default=0)
parser.add_argument('g', type=int, help='background green', nargs='?', default=0)
parser.add_argument('b', type=int, help='background blue', nargs='?', default=0)

args = parser.parse_args()

src_pil = Image.open(args.src_path).convert('RGB')
dst_pil = lib.imagelib.expand_canvas_square(src_pil, args.dst_width, args.r, args.g, args.b)
dst_pil.save(args.dst_path, quality=95)
