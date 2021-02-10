# Make it use the new module:
from computation import compute_heatindex
from printing import print_comparison
from readdata import read_data


# refactor to make more flexible, less hard to change
# add a new key with making changes throughout file

# Column names and column indices to read   index 7
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# data types for each column
# float is a function pointer here, not a function
types = {'tempout':float, 'humout':float, 'heatindex':float}

data = read_data(columns, types=types)
# Now done by read_data
# initialize data variable
# a dictionary, will populate later
# init each list to empty
# data = {}
# for column in columns:
#     # empty list
#     data[column] = []


# filename = "data/wxobs20170821.txt"
# 
# with open(filename, 'r') as datafile:
# # orig    data = datafile.read()
#     # read the first 3 lines (header)
#     #   v a place holder variable (instead of i, j ...) indicates we'll never use the variable
#     for _ in range(3):
#         # could have said 'for i in [0,3]'
#         # print(_)
#         datafile.readline()
# #? What was header read that I missed?
# 
#     # Read and parse the rest of the file
#     # each line is a string
#     for line in datafile:
#         # split along white space
#         split_line = line.split()
#         # add datum to the list 'data'
#         for column in columns:
#             i = columns[column]
#             # there's only one of these
#             t = types.get(column, str)
#             value = t(split_line[i])
#             data[column].append(value)
# 
# 
# # DEBUG
# before calling function; zip  compare lists(?)
# 2 iterators
# for i, j in zip( [1,2], [3,4,5] ):
#     print(i, j)

# Running the function 
# initialize
heatindex = []
for temp, hum in zip( data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, hum))

# compare with precomputed value
# for wc_data, wc_comp in zip(data['windchill'], windchill):
    # formatted print  5 digits after decimal point
    # print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

# output from a function
# Need to know that the first string is limited to 9.
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)

# better output
# zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
# print('               ORIGINAL  COMPUTED')
# print(' DATE    TIME  HEATINDEX HEATINDEX DIFFERENCE')
# print('------- ------ --------- --------- ----------')
# for date, time, hi_orig, hi_comp in zip_data:
#     hi_diff = hi_orig - hi_comp
#     #               time object 6 chars, right justified
#     #                                 9 char, 6 after dec point
#     print(f'{data} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')
# 
    
    

# Some kind debugging or what it would try to do
# d.get(key, str)
# d['key'] --- > str

# print(data['tempout'])

# Debug
# print(data['tempout'])

# % git log --oneline

