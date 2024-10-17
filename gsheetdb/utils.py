def to_dataframe(data):
    """Convert data to a Pandas DataFrame."""
    import pandas as pd
    return pd.DataFrame(data[1:], columns=data[0])


def column_letter(col_num: int) -> str:
    """Convert a column number to a letter (e.g., 1 -> A, 27 -> AA)."""
    letter = ""
    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        letter = chr(65 + remainder) + letter
    return letter