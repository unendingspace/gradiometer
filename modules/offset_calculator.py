
change_start = 500 # sample number where fluxgate movement started
change_end = 700 # sample number where fluxgate movement ended

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

def average(list):
    count = 0.0
    for item in list:
        count += item
    return count / float(len(list))

def findOffset(file):
    test = readFile(file)

    x1 = average(test[1][:change_start])
    y1 = average(test[2][:change_start])
    z1 = average(test[3][:change_start])

    x2 = average(test[1][change_end:])
    y2 = average(test[2][change_end:])
    z2 = average(test[3][change_end:])

    print 'Offsets calculated:'
    print
    print 'X =', (x1 + x2) / 2.0
    print 'Y =', (y1 + y2) / 2.0
    print 'Z =', (z1 + z2) / 2.0

    # one of these will be massive every time, that should be the axis that wasn't reversed




    
