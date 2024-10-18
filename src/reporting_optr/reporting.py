from . import get_date
from . import get_paths
import os
import pandas as pd


class Reports:
    def __init__(self, pattern, directory_path):
        """
        Initializes the Reports class with a regular expression pattern and a directory path.

        Args:
            pattern (re.Pattern): A compiled regular expression pattern used to match file names.
            directory_path (str): The directory path where files are located.
        """
        self.pattern = pattern
        self.directory_path = directory_path
        # self.df = self.validate_and_join_dfs()

    def get_matching_paths(self, file_paths_list, pattern):
        """
        Gets the paths that match the regular expression pattern.

        Uses the 'get_paths' module which includes 'file_paths' and 'match_re' methods.

        Returns:
            list: A list of file paths that match the pattern.

        Time Complexity:
            O(n) - Where 'n' is the number of files in the directory.
        """
        file_paths_list = get_paths.file_paths(self.directory_path)  # """O(n)"""
        paths_list = get_paths.match_re(pattern, file_paths_list)

        return paths_list
    
def get_report_paths(latest_files):
    """
    Retrieve the paths of various report files from the latest_files dictionary.

    Parameters:
    ----------
    latest_files : dict
        A dictionary containing folder names as keys and their latest file paths as values.

    Returns:
    -------
    dict
        A dictionary mapping descriptive variable names to their corresponding file paths.
    """
    return {
        'domestics': latest_files['folder_domestics'],
        'containers': latest_files['folder_containers'],
        '3PLStyles': latest_files['folder_3PLStyles'],
        'stores': latest_files['folder_stores'],
        'ds': latest_files['folder_ds'],
    }