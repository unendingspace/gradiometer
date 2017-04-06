# spectramag2graph
# allows the reading of a spectramag-6 output file (or two) and displaying their results as graphs


import matplotlib.pyplot as plt
import matplotlib as mpl

# reads a spectramag-6 output file into a list of times, x coordinates, y coordinates, and z coordinates

def readFile(filename):
    f = open(filename, 'r')
    times = []
    x = []
    y = []
    z = []
    lines = (f.read().split('\n'))[2:-1] #remove first two lines
    for item in lines:
        item = item.split('\t')
        times.append(float(item[0]))
        x.append(float(item[1]))
        y.append(float(item[2]))
        z.append(float(item[3]))
    f.close()
    return times, x, y, z

# averages a very long list (hopefully)

def findAvg(list):
    print list
    adjust = 0

    if (len(list) == 1): 
            return list[0]
    if (len(list) % 2):
        adjust = list.pop(-1) / (float(len(list)) + 1)
    for index in range(0, len(list) / 2):
        list[index] = (list[index] + list.pop(index + 1))/ 2.0
    print  "Adjust:", adjust
    if (adjust):
        return findAvg(list) * len(list) / (len(list)+1) + adjust
    return findAvg(list)

def findShieldingFactor(file1, file2):
	return 1

print findAvg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 71, 454])
