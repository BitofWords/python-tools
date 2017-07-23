import os
import glob


def get_file_list(dir_path, ext="*", is_full_path=False):
    """
    Return the list of file paths.

    Args:
    - dir_path (str): Directory path.
    - ext (str): Extension. Both include and exclude comma are OK.
    - is_full_path (bool):Return full pash if True, only filename if False.

    Returns:
    - (list of str): List of paths.
    """

    files = glob.glob(os.path.join(dir_path, "*.{}".format(ext)))

    if is_full_path:
        return files
    else:
        return [os.path.basename(f) for f in files]
