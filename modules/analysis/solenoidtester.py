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
    affectedcount = 0
    while (i < len(times) and times[i] < 15):
        unaffected += data[i]
        unaffectedcount += 1
        i += 1

    while (i < len(times) and times[i] < 25):
        i += 1

    while (i < len(times) and times[i] < 35):
        affected += data[i]
        affectedcount += 1
        i += 1

    while (i < len(times) and times[i] < 45):
        i += 1

    while (i < len(times)):
        unaffected += data[i]
        unaffectedcount += 1
        i += 1

    change = int(affected / affectedcount - unaffected / unaffectedcount)

    print
    print "Average before/after:", unaffected/unaffectedcount
    print "Average during:", affected/affectedcount
    print "Change:", str(change) + "nT"
    print


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


readout('/home/mpalmer/test1/solenoid_map/side/998mV7or8mA.Dat', 'y')
