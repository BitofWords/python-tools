import numpy as np
from PIL import Image


def read_img_to_ndarray(path):
    return np.array(Image.open(path))


def save_ndarray_as_img(array, path, **kwargs):
    Image.fromarray(np.uint8(array)).save(path, **kwargs)
