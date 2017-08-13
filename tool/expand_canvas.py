#!/usr/bin/env python3

import argparse

from PIL import Image

import lib.imagelib

"""
Expand canvas of image.
usage: expand_canvas.py [-h]
                        src_path dst_path dst_width dst_height [pos_x] [pos_y]
                        [r] [g] [b]
"""

parser = argparse.ArgumentParser(
    description='Expand canvas.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('src_path', help='path of src image')
parser.add_argument('dst_path', help='path of dst image')
parser.add_argument('dst_width', type=int, help='width of dst image')
parser.add_argument('dst_height', type=int, help='height of dst image')
parser.add_argument('pos_x', type=int, help='pasted position x', nargs='?', default=0)
parser.add_argument('pos_y', type=int, help='pasted position y', nargs='?', default=0)
parser.add_argument('r', type=int, help='background red', nargs='?', default=0)
parser.add_argument('g', type=int, help='background green', nargs='?', default=0)
parser.add_argument('b', type=int, help='background blue', nargs='?', default=0)

args = parser.parse_args()

src_pil = Image.open(args.src_path).convert('RGB')
dst_pil = lib.imagelib.expand_canvas(
    src_pil, args.dst_width, args.dst_height, args.pos_x, args.pos_y, args.r, args.g, args.b)
dst_pil.save(args.dst_path, quality=95)
