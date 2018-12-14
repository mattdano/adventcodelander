import numpy as np
data = np.genfromtxt("./input_6.txt",delimiter=',',dtype=int)
#print(data)
#type(data[0][0])

def manhattan_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def get_nearest(point):
    lowest=1000
    for pid,p in enumerate(data):
        distance = manhattan_distance(point,p)
        if distance<lowest:
            lowest=distance
            best=pid
        elif distance==lowest:
            return '-1'

    return best



maxx = np.max(data[:,0])
maxy = np.max(data[:,1])
minx = np.min(data[:,0])
miny = np.min(data[:,1])

print(minx,maxx,miny,maxy)

grid = np.ones((maxx,maxy))*-2

for x in range(minx,maxx):
    for y in range(miny,maxy):

        #manhattan_distance(data[0],i)
        grid[x,y] = get_nearest([x,y])

print(grid)
import matplotlib.pyplot as plt
#plt.imshow(grid)
#plt.show()
areas=[]
for i in range(0,len(data)):
    areas.append(np.sum((grid==i)))

print('Biggest area:',max(areas))
region=0
for i in range(maxx + 1):
    for j in range(maxy+ 1):
        region += int(sum(abs(data[:,0] - i) + abs(data[:,1] - j)) < 10000)


print(region)
