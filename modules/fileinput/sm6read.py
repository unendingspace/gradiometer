# Tools for reading in Spectramag-6 .Dat files

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
        if (item[1] == '-1.#INF'):
            continue
            # these always occur in threes (over all axes) for some reason, or at least they appear to
            # also, just skipping the might not be the best approach

        x.append(float(item[1]))
        y.append(float(item[2]))
        z.append(float(item[3]))
    f.close()
    return times, x, y, z