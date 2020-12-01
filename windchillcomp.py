# refactor to make more flexible, less hard to change
# add a new key with making changes throughout file

# Column names and column indices to read   index 7
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# data types for each column
# float is a function pointer here, not a function
type = {'tempout': float, 'windspeed':float, 'windchill':float}

# initialize data variable
# a dicionary, will populate later
# init each list to empty
data = {}
for column in columns:
    # empty list
    data[column] = []


filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
# orig    data = datafile.read()
    # read the first 3 lines (header)
    #   v a place holder variable (instead of i, j ...) indicates we'll never use the variable
    for _ in range(3):
        # could have said 'for i in [0,3]'
        # print(_)
        datafile.readline()
#? What was header read that I missed?

    # Read and parse the rest of the file
    # each line is a string
    for line in datafile:
        # split along white space
        split_line = line.split()
        # add datum to the list 'data'
        for column in columns:
            i = columns[column]
            # there's only one of these
            t = type.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

# Calc wind chill
# Use verbs for function names.
def compute_windchill(t, v):
    # constants
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    # new variable
    v16 = v **0.16

    wci = a + (b*t) - (c * v16) + (d * t * v16)
    return wci

# DEBUG
# before calling function; zip  compare lists(?)
# 2 iterators
for i, j in zip( [1,2], [3,4,5] ):
    print(i, j)

# Running the function 
# initialize
windchill = []
for temp, windspeed in zip( data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# print(windchill)

# compare with precomputed value
# for wc_data, wc_comp in zip(data['windchill'], windchill):
    # formatted print  5 digits after decimal point
    # print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

# better output
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
print('               ORIGINAL  COMPUTED')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    #               time object 6 chars, right justified
    #                                 9 char, 6 after dec point
    print(f'{data} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')

    
    

# Some kind debugging or what it would try to do
# d.get(key, str)
# d['key'] --- > str

# print(data['tempout'])

# Debug
# print(data['tempout'])

# % git log --oneline
