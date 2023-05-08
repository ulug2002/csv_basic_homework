#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data = data.split('\n')
    res = []
    for i in data:
        res.append(i.split(',')[0])
    return res
data = open('data.csv').read()