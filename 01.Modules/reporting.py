import get_date
import get_paths
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
        self.df = self.validate_and_join_dfs()