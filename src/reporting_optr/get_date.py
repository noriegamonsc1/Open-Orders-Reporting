import re


def extract_date_path(path):
    """
    Extracts a date from a file path based on a specific pattern.

    Args:
        path (str): The file path from which to extract the date.

    Returns:
        str: A date string in the format "YYYYMMDD" extracted from the path, or "00000000" if no date is found.

    Notes:
        The function looks for an 8-digit date pattern (YYYYMMDD) within the file path. 
        If a date is found, it returns the first match. If no match is found, it returns "00000000".

    Time Complexity:
        O(1) - The time complexity is constant as it performs a fixed number of regex operations on a given string.
    """
    pattern = r"(\d{2}\.\d{2}\.\d{4}|\d{8})"
    if re.search(pattern, path):
        return re.search(pattern, path).group()
    else:
        return "00000000"


if __name__ == "__main__":
    print(f"{__name__} was run as a module")

else:
    print(f"{__name__} was imported as a module")
