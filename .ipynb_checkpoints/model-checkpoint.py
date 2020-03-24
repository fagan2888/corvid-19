import pandas as pd

def read_data(url):
    """
    Read Covid19 data.
    
    Parameters
    ----------
    url: str
    
    Returns
    -------
    pd.DataFrame
    """
    data = pd.read_csv(url)
    data = data.iloc[:, [1, *range(4, data.shape[1])]]
    data = data.set_index(data.columns[0])
    data = data.groupby(data.index).sum()
    data = data.T
    data.index = pd.to_datetime(data.index)
    
    return data