# spectramag2graph
# allows the reading of a spectramag-6 output file (or two) and displaying their results as graphs


import matplotlib.pyplot as plt
import matplotlib as mpl

halftime = 120

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


def rollingAvg(meas, points):
	avgmeas = []
	for num, item in enumerate(meas):
		if num > points/2 and num < len(meas) - points/2:
			avgmeas.append(sum(meas[num-points/2:num+points/2]) / len(meas[num-points/2:num+points/2]))
	return avgmeas

def getRollingTime(time, points):
	return time[points/2+1:len(time)-points/2]

# transmutes time axis to fold in quarters

def quarterTimes(lst):
    max = lst[-1]
    for num, item in enumerate(lst):
        if (item <= max/4):
            continue
        elif (item <= max/2):
            lst[num] = max/2 - item
        else:
            lst[num] = max - item
    return lst

# transmutes time axis to fold in half

def halfTimes(lst):
    max = lst[-1]
    for num, item in enumerate(lst):
        if (item > halftime):
            lst[num] = halftime - item
    return lst

# plots fluxgate readings
# time axis is whole of measurement time

def plotFlux(t, x, y, z):

    print 'Plotting'

    mpl.rcParams['toolbar'] = 'None'

    plt.figure(1)
    plt.subplot(311)
    plt.title('X Direction')
    plt.xlabel('Time (s)')
    plt.ylabel('Flux (nT)')
    plt.plot(t, x, 'r-')

    plt.subplot(312)
    plt.title('Y Direction')
    plt.xlabel('Time (s)')
    plt.ylabel('Flux (nT)')
    plt.plot(t, y, 'b-')

    plt.subplot(313)
    plt.title('Z Direction')
    plt.xlabel('Time (s)')
    plt.ylabel('Flux (nT)')
    plt.plot(t, z, 'g-')

    #plt.tight_layout()

    plt.show()
    plt.close()

def analyze(x, y, z, t):
	# find halftime win max zs
	max1 = 0
	max2 = 0
	t1 = -1
	t2 = -1
	for num, item in enumerate(y):
		if (num < (len(y) / 2)):
			if item > max1 or t1 < 0:
				max1 = item
				t1 = num 
		else:
			if item > max2 or t2 < 0:
				max2 = item
				t2 = num


	min1 = 'a'
	min2 = 'a'
	for num, item in enumerate(y):
		if num < len(y)/4:
			if min1 == 'a':
				min1 = item
			elif item < min1:
				min1 = item
		if num > len(y)*3/4:
			if min2 == 'a':
				min2 = item
			elif item < min2:
				min2 = item
	response = (abs(max1 - min1) + abs(max2 - min2))/2

	print 'Y Response: ' + str(response) + 'nT'

	zmax1 = max(z[t1 - 1000:t1 + 1000])
	zmax2 = max(z[t2 - 1000:t2 + 1000])
	zmin1 = min(z[t1 - 1000:t1 + 1000])
	zmin2 = min(z[t2 - 1000:t2 + 1000])
	
	print 'Z Response: ' + str((abs(zmax1 - zmin1) + abs(zmax2 - zmin2))/2.0) + 'nT' 

def getError(dataset):
	error = 0
	for num, item in enumerate(dataset[:len(dataset)-1]):
		temp = abs(dataset[num+1] - item)
		if temp > error:
			error = temp
	return error		

# combines and plots two matching fluxgate readouts in the following manner:
# x = x1 + x2
# y = y1 - y2
# z = z1 + z2

def readout(x1, y1, z1, t1, x2, y2, z2, t2):

    for idx in range(0, len(x2)):
        x1[idx] = x1[idx] + x2[idx]
        y1[idx] = y1[idx] - y2[idx]
        z1[idx] = z1[idx] + z2[idx]

    error = getError(y1) / 50.0
    print 'Error in Y-axis measurement: +/-' + str(error) + 'nT'

    print 'Error in Z-axis measurement: +/-' + str(getError(z1)/50.0) + 'nT'
	
 
    analyze(x1, y1, z1, t1)

    plotFlux(t1, x1, y1, z1)

def temp(txt):
	file1 = readFile('/ucnscr/mpalmer/gradiodata/laptoptests/runs/' + txt +'plastic/IN1.Dat')
	
	file2 = readFile('/ucnscr/mpalmer/gradiodata/laptoptests/runs/' + txt +'plastic/IN2.Dat')

	readout(file1[1], file1[2], file1[3], file1[0], file2[1], file2[2], file2[3], file2[0])

def main():
	file1 = readFile('/ucnscr/mpalmer/gradiodata/laptoptests/runs/200mVplastic/IN1.Dat')
	file2 = readFile('/ucnscr/mpalmer/gradiodata/laptoptests/runs/200mVplastic/IN2.Dat') 

	readout(file1[1], file1[2], file1[3], file1[0], file2[1], file2[2], file2[3], file2[0])

