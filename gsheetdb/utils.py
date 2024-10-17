def to_dataframe(data):
    """Convert data to a Pandas DataFrame."""
    import pandas as pd
    return pd.DataFrame(data[1:], columns=data[0])
