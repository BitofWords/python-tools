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


def save_gradation_img(width, height, start_color, stop_color, is_horizontal, path='gradation.bmp', **kwargs):
    a = nplib.get_gradation_3d(width, height, start_color, stop_color,
                               (is_horizontal, is_horizontal, is_horizontal),
                               'uint8')
    save_ndarray_as_img(a, path, **kwargs)


def expand_canvas(src_pil, dst_width, dst_height, pos_x=0, pos_y=0, r=0, g=0, b=0):
    canvas = Image.new('RGB', (dst_width, dst_height), (r, g, b))
    canvas.paste(src_pil, (pos_x, pos_y))
    return canvas
