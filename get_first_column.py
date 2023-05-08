def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data =  data.split('\n')
    a = []
    for i in data:
        a.append(i.split(',')[0])
    return a 

# Read the csv file
data = open('data.csv').read()
print(get_first_column(data))