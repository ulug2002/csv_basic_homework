def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    data = data.split('\n')
    l = []
    for i in data:
        b = i.split(',')
        l.append(b)
    return len(data)-1
data = open('data.csv').read()
# Read the csv file
print(find_number_of_rows(data))