import sys
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

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


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def mask_circle_solid(pil_img, background_color, blur_radius, offset=0):
    background = Image.new(pil_img.mode, pil_img.size, background_color)
    
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    
    return Image.composite(pil_img, background, mask)


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    
    result = pil_img.copy()
    result.putalpha(mask)
    
    return result
