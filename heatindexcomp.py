# Make it use the new module:
from mysci.computation import compute_heatindex
from mysci.printing import print_comparison
from mysci.readdata import read_data


# refactor to make more flexible, less hard to change
# add a new key with making changes throughout file

# Column names and column indices to read   index 7
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex':13}

# data types for each column
# float is a function pointer here, not a function
types = {'tempout':float, 'humout':float, 'heatindex':float}

data = read_data(columns, types=types)

# Running the function 
# initialize
# heatindex = []
# for temp, hum in zip( data['tempout'], data['humout']):
#     heatindex.append(compute_heatindex(temp, hum))
# A comprehension
heatindex = [compute_heatindex(t, h)) for t, h in zip( data['tempout'], data['humout'])]

# compare with precomputed value
# for wc_data, wc_comp in zip(data['windchill'], windchill):
    # formatted print  5 digits after decimal point
    # print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

# output from a function
# Need to know that the first string is limited to 9.
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)


# Some kind debugging or what it would try to do
# d.get(key, str)
# d['key'] --- > str

# print(data['tempout'])

# Debug
# print(data['tempout'])

# % git log --oneline

