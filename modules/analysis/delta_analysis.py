
import matplotlib.pyplot as plt

plt.rcParams['toolbar'] = 'None'

change_start = 500 # sample number where fluxgate movement started
change_end = 700 # sample number where fluxgate movement ended

def average(list):
    count = 0.0
    for item in list:
        count += item
    return count / float(len(list))

def getSimpleFileName(filename):
    slash = 0
    dot = len(filename)
    for i in range(0, len(filename)):
        if filename[i] == '/':
            slash = i
        elif filename[i] == '.':
            dot = i
    return filename[slash+1:dot]

def plotFlux(dx, dy, dz, innum):

    fig = plt.figure(1, figsize=(16, 10))
    fig.canvas.set_window_title('Delta Analysis')

    plt.subplot(3, 2, innum)
    plt.yscale('log')
    plt.title('Input ' + str(innum) + ' X')
    plt.xlabel('Delta Bx (nT)')
    plt.ylabel('Count')
    plt.hist(dx, bins=200, normed=0, facecolor='red') #used to have bins=range(min(dx), max(dx) + 0.1, 0.1)
    #plt.axis([min(dx), max(dx), 0, 25000])

    plt.subplot(3, 2, innum+2)
    plt.yscale('log')
    plt.title('Input ' + str(innum) + ' Y')
    plt.xlabel('Delta By (nT)')
    plt.ylabel('Count')
    plt.hist(dy, bins=200, normed=0, facecolor='blue')
    #plt.axis([min(dy), max(dy), 0, 25000])

    plt.subplot(3, 2, innum+4)
    plt.yscale('log')
    plt.title('Input ' + str(innum) + ' Z')
    plt.xlabel('Delta Bz (nT)')
    plt.ylabel('Count')
    plt.hist(dz, bins=200, normed=0, facecolor='yellow')
    #plt.axis([min(dz), max(dz), 0, 25000])

    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.6)

def takeSlope(x, y, z, innum):
    dx = []
    dy = []
    dz = []

    if len(x) != len(y) or len(y) != len(z):
        return -1

    for i in range(0, len(x) - 1):
        a = x[i+1]-x[i]
        b = y[i+1]-y[i]
        c = z[i+1]-z[i]

        #bad version of outlier bins:

        if abs(a) > 100:
            a = 99 * a / abs(a)
        if abs(b) > 100:
            b = 99 * b / abs(b)
        if abs(c) > 100:
            c = 99 * c / abs(c)

        dx.append(a)
        dy.append(b)
        dz.append(c)

    return dx, dy, dz, innum

# takes list of t x y zs
# ex. [[t2s], [x1s], [y1s], [z1s], [t2s] etc]

def analyze(readins):
    for num, readin in enumerate(readins):
        plotFlux(*takeSlope(readin[1], readin[2], readin[3], num + 1))
    plt.show()
    plt.close()

#analyze(['/media/ASDF/data/stacked/stacked2_out1.Dat', '/media/ASDF/data/stacked/stacked2_out2.Dat'])

