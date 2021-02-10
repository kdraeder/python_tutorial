
# Read the data line
# create var
filename = "data/wxobs20170821.txt"
# open it in read mode   w(rite) 
datafile = open(filename, 'r')

# Read first line
print(datafile.readline())
# Read second line
print(datafile.readline())
# Read third line
print(datafile.readline())
# Read fourth line
print(datafile.readline())

datafile.close()
