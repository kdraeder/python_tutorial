# def read_data(columns, types{}, filename="data/wxobs20170821.txt"):
def read_data(columns, types, filename="data/wxobs20170821.txt"):
    #                             ^ keyword argument; don't have to enter it
    # Docstring:
    """
    Read the data from CU Boulder weather station file
    Parameters:
        columns: a dictionary of column names mapping to column indices
        types:   dict of col names mapping to the types to which to convert each col of data
        filename: a string path pointing to the CU Boulder Weather Station data file
    """

    # initialize data variable
    # a dicionary, will populate later
    # init each list to empty
    data = {}
    for column in columns:
        # empty list
        data[column] = []

    with open(filename, 'r') as datafile:
        # read the first 3 lines (header)
        #   v a place holder variable (instead of i, j ...) indicates we'll never use the variable
        for _ in range(3):
            # could have said 'for i in [0,3]'
            # print(_)
            datafile.readline()

        # Read and parse the rest of the file
        # each line is a string
        for line in datafile:
            # split along white space
            split_line = line.split()
            # add datum to the list 'data'
            for column in columns:
                i = columns[column]
                t = types.get(column, str)
                value = t(split_line[i])
                data[column].append(value)
            
    return data
