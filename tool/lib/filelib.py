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


def add_prefix(prefix, org_path):
    """
    Add prefix to filename.

    Args:
    - prefix (str): String of prefix.
    - org_path (str): Original path.

    Returns:
    - new_path (str): Path with prefix.
    """

    new_path = os.path.join(os.path.dirname(org_path),
                            prefix + os.path.basename(org_path))
    os.rename(org_path, new_path)
    return new_path


def add_prefix_batch(prefix, dir_path='.', ext='*'):
    """
    Add prefix to filename of files at the directory with the extension.

    Args:
    - prefix (str): String of prefix.
    - dir_path (str): Directory path.
    - ext (str): Extension. Both include and exclude comma are OK.

    Returns:
    - None
    """

    files = get_file_list(dir_path, ext, True)

    for f in files:
        new_path = add_prefix(prefix, f)
        print("{} > {}".format(f, new_path))
