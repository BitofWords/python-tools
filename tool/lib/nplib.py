import numpy as np


def get_max_and_pos_2d(array):
    width = array.shape[1]
    max_val = array.max()
    y, x = divmod(np.argmax(array), width)
    return (max_val, (x, y))


def get_min_and_pos_2d(array):
    width = array.shape[1]
    min_val = array.min()
    y, x = divmod(np.argmin(array), width)
    return (min_val, (x, y))


def get_max_and_pos_3d(array):
    channel_num = array.shape[2]
    max_list = [None] * channel_num
    max_pos_list = [None] * channel_num
    for i in range(channel_num):
        (max_list[i], max_pos_list[i]) = get_max_and_pos_2d(array[:, :, i])
    return (tuple(max_list), tuple(max_pos_list))


def get_min_and_pos_3d(array):
    channel_num = array.shape[2]
    min_list = [None] * channel_num
    min_pos_list = [None] * channel_num
    for i in range(channel_num):
        (min_list[i], min_pos_list[i]) = get_min_and_pos_2d(array[:, :, i])
    return (tuple(min_list), tuple(min_pos_list))


def expand_canvas(src_array, dst_width, dst_height, src_pos_x=0, src_pos_y=0):
    src_height, src_width, src_channel = src_array.shape
    dst_array = np.zeros((dst_height, dst_width, src_channel), dtype=src_array.dtype)
    dst_array[src_pos_y:src_pos_y+src_height, src_pos_x:src_pos_x+src_width] = src_array
    return dst_array


def get_gradation_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradation_3d(width, height, start_list, stop_list, is_horizontal_list, dtype):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradation_2d(start, stop, width, height, is_horizontal)

    return result.astype(dtype)
