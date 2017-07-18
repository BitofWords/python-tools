import os
import glob


def get_file_list(dir_path, ext="*", is_full_path=False):
    files = glob.glob(os.path.join(dir_path, "*.{}".format(ext)))

    if is_full_path:
        return files
    else:
        return [os.path.basename(f) for f in files]
