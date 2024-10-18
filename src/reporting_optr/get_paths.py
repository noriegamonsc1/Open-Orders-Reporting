import os
from . import get_date
import re


def file_paths(directory_path, file_paths_list=None):
    """
    Recursively collects and returns a sorted list of file paths from a directory and its subdirectories.

    Args:
        directory_path (str): directory's path from which to collect the file paths.
        file_paths_list (list, optional): list to store the collected file paths. If not provided, an empty list is initialized.

    Returns:
        list: a sorted list of the file paths.

    Notes:
        The function traverses each folder in the given directory path. If it finds a subdirectory, it makes a recursive call.
        If it finds a file, it appends the file's path to the list. After collecting all file paths, it sorts them based on the dates using the get_date.py.

    Time complexity:
         O(n log n) - n is the total number of files and directories. The sorting operation dominates the time complexity
    """
    if file_paths_list is None:
        file_paths_list = []

    for folder in os.listdir(directory_path):
        path = os.path.join(directory_path, folder)
        if os.path.isdir(path):
            file_paths(path, file_paths_list)
        else:
            file_paths_list.append(path)

    file_paths_list = sorted(file_paths_list, key=get_date.extract_date_path)
    return file_paths_list


def match_re(pattern, list_paths):
    """
    Filters a list of file paths based on a given regular expression pattern.

    Args:
        pattern (re.Pattern): A compiled regular expression pattern to match against filenames.
        list_paths (list): A list of file paths to be filtered.

    Returns:
        list: A list of file paths where filenames match the given pattern.

    Notes:
        The function iterates through each path in the list, extracts the filename, and checks if the filename matches the pattern using 
        the `search` method from the `re` module. It appends the paths of matching files to a new list.

    Time Complexity:
        O(m * p) - `m` is the number of file paths in `list_paths` and `p` is the average length of the filenames being checked against the pattern. 
        The regular expression search operation can vary in complexity depending on the pattern used.
    """
    paths_list = []
    for path in list_paths:
        filename = os.path.basename(path)
        if pattern.search(filename): # changed from 'match' to 'search'
            paths_list.append(path)

    return paths_list


if __name__ == "__main__":
    print(f"{__name__} was run as a module")

else:
    print(f"{__name__} was imported as a module")
