import os
import sys
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


def rename_with_confirm(org_and_new_path_list):
    """
    Rename file with using list after confirm.
    Input y or yes, rename.

    Args:
    - org_and_new_path_list (list): List of lists.
        [[org_path1, new_path1], [org_path2, new_path2], ...]

    Returns:
    - None
    """

    answer = input("yes? ")
    if answer in ["y", "yes"]:
        rename_without_confirm(org_and_new_path_list)
    else:
        print("skip")


def rename_without_confirm(org_and_new_path_list):
    """
    Rename file with using list.

    Args:
    - org_and_new_path_list (list): List of lists.
        [[org_path1, new_path1], [org_path2, new_path2], ...]

    Returns:
    - None
    """

    for path in org_and_new_path_list:
        os.rename(path[0], path[1])
    print("done")


def get_prefix_suffix_added_path(org_path, prefix='', suffix=''):
    """
    Get prefix or/and suffix added path.

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
    return new_path


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

    new_path = get_prefix_suffix_added_path(org_path, prefix, suffix)
    os.rename(org_path, new_path)
    return new_path


def add_prefix_suffix_batch(prefix='', suffix='', dir_path='.', ext='*', is_confirm=True):
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
    if len(files) == 0:
        sys.exit('no file')

    org_and_new_path_list = []
    for f in files:
        new_path = get_prefix_suffix_added_path(f, prefix, suffix)
        org_and_new_path_list.append([f, new_path])
        print("{} > {}".format(f, new_path))

    if is_confirm:
        rename_with_confirm(org_and_new_path_list)
    else:
        rename_without_confirm(org_and_new_path_list)
