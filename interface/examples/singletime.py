import matplotlib.pyplot as plt
import matplotlib as mpl

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

def halfTimes(lst):
    max = lst[-1]
    for num, item in enumerate(lst):
        if (item > max/2):
            lst[num] = max - item
    return lst

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

def plusMinusPlusComb(file1, file2):
    data1 = readFile(file1)
    data2 = readFile(file2)

    if (len(data1) != len(data2)):
        print "Error: files do not match"
        return -1

    for idx in range(0, len(data1)):
        data1[1][idx] = data1[1][idx] + data2[1][idx]
        data1[2][idx] = data1[2][idx] + data2[2][idx]
        data1[3][idx] = data1[3][idx] + data2[3][idx]

    plotFlux(halfTimes(data1[0]), data1[1], data1[2], data1[3])

plusMinusPlusComb('/mnt/win/Users/Matthew/Desktop/sfi1.Dat', '/mnt/win/Users/Matthew/Desktop/sfi2.Dat')