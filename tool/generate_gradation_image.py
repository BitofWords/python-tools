#!/usr/bin/env python3

import argparse

import lib.imagelib

parser = argparse.ArgumentParser(
    description='Generate gradation image.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('width', type=int, help='width')
parser.add_argument('height', type=int, help='height')
parser.add_argument('start_red', type=int, help='start red')
parser.add_argument('start_green', type=int, help='start green')
parser.add_argument('start_blue', type=int, help='start blue')
parser.add_argument('stop_red', type=int, help='stop red')
parser.add_argument('stop_green', type=int, help='stop green')
parser.add_argument('stop_blue', type=int, help='stop blue')
parser.add_argument('is_horizontal', type=bool, help='is_horizontal')
parser.add_argument('path', help='path', nargs='?', default='out.bmp')
parser.add_argument('quality', type=int, help='quality for jpg', nargs='?')

args = parser.parse_args()

kwargs = {}
if args.quality is not None:
    kwargs['quality'] = args.quality

lib.imagelib.save_gradation_img(
    args.width, args.height,
    (args.start_red, args.start_green, args.start_blue),
    (args.stop_red, args.stop_green, args.stop_blue),
    args.is_horizontal, args.path, **kwargs
)
