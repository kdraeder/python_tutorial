# Make it use the new module:
from readdata import read_data
from printing import print_comparison
from computation import compute_windchill

# refactor to make more flexible, less hard to change
# add a new key with making changes throughout file

# Column names and column indices to read   index 7
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# data types for each column
# float is a function pointer here, not a function
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read data from file
data = read_data(columns, types=types)

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

# output from a function
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)

# better output
# Now in a function in printing.py
# zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
# print('               ORIGINAL  COMPUTED')
# print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
# print('------- ------ --------- --------- ----------')
# for date, time, wc_orig, wc_comp in zip_data:
#     wc_diff = wc_orig - wc_comp
#     #               time object 6 chars, right justified
#     #                                 9 char, 6 after dec point
#     print(f'{data} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')
# 
#     
    

# Some kind debugging or what it would try to do
# d.get(key, str)
# d['key'] --- > str

# print(data['tempout'])

# Debug
# print(data['tempout'])

# % git log --oneline
