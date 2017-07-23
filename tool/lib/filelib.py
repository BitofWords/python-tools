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

    if ext[0] == '.':
        ext = ext[1:]

    files = glob.glob(os.path.join(dir_path, "*.{}".format(ext)))

    if is_full_path:
        return files
    else:
        return [os.path.basename(f) for f in files]


def add_prefix_suffix(org_path, prefix='', suffix=''):
    """
    Add prefix or/and suffix to filename.

    Args:
    - org_path (str): Original path.
    - prefix (str): String of prefix.
    - suffix (str): String of suffix.

    Returns:
    - new_path (str): Path with prefix or/and suffix.
    """

    dirname = os.path.dirname(org_path)
    basename = os.path.basename(org_path)
    root, ext = os.path.splitext(basename)
    new_path = os.path.join(dirname, prefix + root + suffix + ext)
    os.rename(org_path, new_path)
    return new_path


def add_prefix_suffix_batch(prefix='', suffix='', dir_path='.', ext='*'):
    """
    Add prefix or/and suffix to filename of files at the directory with the extension.

    Args:
    - prefix (str): String of prefix.
    - suffix (str): String of suffix.
    - dir_path (str): Directory path.
    - ext (str): Extension. Both include and exclude comma are OK.

    Returns:
    - None
    """

    files = get_file_list(dir_path, ext, True)

    for f in files:
        new_path = add_prefix_suffix(f, prefix, suffix)
        print("{} > {}".format(f, new_path))
