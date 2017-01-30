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
        times.append(item[0])
        x.append(item[1])
        y.append(item[2])
        z.append(item[3])
    f.close()
    return times, x, y, z

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

a = readFile('/mnt/win/Users/Matthew/Desktop/asdf.Dat')

plotFlux(a[0], a[1], a[2], a[3])