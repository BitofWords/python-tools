import sys
import os

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import nplib


def read_img_to_ndarray(path):
    return np.array(Image.open(path))


def save_ndarray_as_img(array, path, **kwargs):
    Image.fromarray(np.uint8(array)).save(path, **kwargs)


def save_gradation_img(width, height, start_color, stop_color, is_horizontal_list, path='gradation.bmp', **kwargs):
    a = nplib.get_gradation_3d(width, height, start_color, stop_color, is_horizontal_list)
    save_ndarray_as_img(a, path, **kwargs)


def expand_canvas(src_pil, dst_width, dst_height, pos_x=0, pos_y=0, r=0, g=0, b=0):
    canvas = Image.new('RGB', (dst_width, dst_height), (r, g, b))
    canvas.paste(src_pil, (pos_x, pos_y))
    return canvas


def expand_canvas_square(src_pil, dst_width, r=0, g=0, b=0):
    width, height = src_pil.size
    if width > height:
        new_width = dst_width
        new_height = int(height * dst_width / width)
        pos_x = 0
        pos_y = int((dst_width - new_height) / 2)
    else:
        new_height = dst_width
        new_width = int(width + dst_width / height)
        pos_x = int((dst_width - new_width) / 2)
        pos_y = 0
    resized_src_pil = src_pil.resize((new_width, new_height), Image.BICUBIC)
    dst_pil = expand_canvas(
        resized_src_pil, dst_width, dst_width, pos_x, pos_y, r, g, b)
    return dst_pil


def add_margin(im, top, right, bottom, left, color):
    width, height = im.size
    new_width = width + right + left
    new_height = height + top + bottom
    im_new = Image.new(im.mode, (new_width, new_height), color)
    im_new.paste(im, (left, top))
    return im_new


def expand2square(im, background_color):
    width, height = im.size
    if width == height:
        return im
    elif width > height:
        im_new = Image.new(im.mode, (width, width), background_color)
        im_new.paste(im, (0, (width - height) // 2))
        return im_new
    else:
        im_new = Image.new(im.mode, (height, height), background_color)
        im_new.paste(im, ((height - width) // 2, 0))
        return im_new
