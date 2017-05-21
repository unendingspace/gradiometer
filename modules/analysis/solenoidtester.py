# spectramag2graph
# allows the reading of a spectramag-6 output file (or two) and displaying their results as graphs


import matplotlib.pyplot as plt
import matplotlib as mpl

halftime = 20
buffertime = 2

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



# plots fluxgate readings
# time axis is whole of measurement time

def plotFlux(t, axisname, meas):

    mpl.rcParams['toolbar'] = 'None'

    plt.figure(1)
    plt.title(axisname.upper() + ' Direction')
    plt.xlabel('Time (s)')
    plt.ylabel('Flux (nT)')
    plt.plot(t, meas, 'g-')

    plt.show()
    plt.close()

def roughReading(data, times):
    i = 0
    unaffected = 0.0
    affected = 0.0
    unaffectedcount = 0
    affectedmax = -10000
    affectedmin = 10000
    unaffectedmax = -10000
    unaffectedmin = 10000
    affectedcount = 0
    while (i < len(times) and times[i] < halftime - buffertime):
	if data[i] < unaffectedmin:
		unaffectedmin = data[i]
	if data[i] > unaffectedmax:
		unaffectedmax = data[i]
        unaffected += data[i]
        unaffectedcount += 1
        i += 1

    while (i < len(times) and times[i] < halftime + buffertime):
        i += 1

    while (i < len(times)):
	if data[i] > affectedmax:
		affectedmax = data[i]
	if data[i] < affectedmin:
		affectedmin = data[i]
        affected += data[i]
        affectedcount += 1
        i += 1

    change = int(affected / affectedcount - unaffected / unaffectedcount)
    error = abs((affectedmax - affectedmin) / 2.0) + abs((unaffectedmax - unaffectedmin) / 2.0) 

    print
    print "Average before/after:", unaffected/unaffectedcount
    print "Average during:", affected/affectedcount
    print "Change:", str(change) + "nT"
    print
    print 'Error:', str(error) + 'nT'
    print

def readout2(filename, axis):
	data = readFile(filename)
	axis_num = 0
	if axis == 'x':
		axis_num = 1
	elif axis == 'y':
		axis_num = 2
	else:
		axis_num = 3
	changecount = 0
	changesum = 0
	biggestchange = 0
	biggest = 0
	biggesttime = 0
	for i in range(0, len(data[0]) - 1):
		change = abs(data[axis_num][i+1] - data[axis_num][i])
		if (data[0][i] <= halftime + buffertime and data[0][i] >= halftime - buffertime and change > biggest):
			if (biggest != 0):
				changecount += 1
				changesum += biggest
				biggestchange = biggest
			biggest = change
			biggesttime = data[0][i]
		else:
			changecount += 1
			changesum += change
			if biggestchange == 0:
				biggestchange = change
	print
	print 'The biggest change occurred at', biggesttime, 'and was', str(biggest) + 'nT in magnitude.'
	print				
	print 'The margin of error was +/-', str(biggestchange) + 'nT.'
	print
	plotFlux(data[0], axis, data[axis_num])


def readout(filename, axis):
    data = readFile(filename)
    if axis == 'x':
        roughReading(data[1], data[0])
        plotFlux(data[0], axis, data[1])
    elif axis == 'y':
        roughReading(data[2], data[0])
        plotFlux(data[0], axis, data[2])
    elif axis == 'z':
        roughReading(data[3], data[0])
        plotFlux(data[0], axis, data[3])
    else:
        print
        print 'No.'
        print
        exit()

if __name__ == '__main__':
	readout('/home/mpalmer/test1/solenoid_map/side/998mV7or8mA.Dat', 'y')
