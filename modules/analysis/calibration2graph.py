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

# transmutes time axis to fold in quarters

def quarterTimes(lst):
    max = lst[-1]
    for num, item in enumerate(lst):
        if (item <= max/4):
            continue
        elif (item <= max/2):
            lst[num] = max/2 - item
        elif (item <= 3*max/4):
            lst[num] = item - max/2
        else:
            lst[num] = max - item
    return lst

# transmutes time axis to fold in half

def halfTimes(lst):
    max = lst[-1]
    for num, item in enumerate(lst):
        if (item > max/2):
            lst[num] = max - item
    return lst

# plots fluxgate readings
# time axis is whole of measurement time

def plotFlux(t, x, y, z):

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

    plt.tight_layout()

    plt.show()
    plt.close()

# combines and plots two matching fluxgate readouts in the following manner:
# x = x1 + x2
# y = y1 - y2
# z = z1 + z2

def readout(x1, y1, z1, t1, x2, y2, z2, t2):

    if (len(data1) != len(data2)):
        print "Error: files do not match"
        return -1

    for idx in range(0, len(data1)):
        x1[idx] = x1[idx] + x2[idx]
        y1[idx] = y1[idx] - y2[idx]
        z1[idx] = z1[idx] + z2[idx]

    plotFlux(t1, x1, y1, z1)

def main():
	file1 = readFile('/ucnscr/mpalmer/gradiodata/14.56-21.04.2017solenoidoff/IN1.Dat')
	file2 = readFile('/ucnscr/mpalmer/gradiodata/14.56-21.04.2017solenoidoff/IN2.Dat')

	readout(file1[1], file1[2], file1[3], halfTimes[file1[0]], file2[1], file2[2], file2[3], file2[0])
