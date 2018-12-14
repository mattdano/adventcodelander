from collections import defaultdict
import matplotlib.pyplot as plt

f = open('./input_10.txt','r')
lines = f.readlines()

print(lines)

posvel = defaultdict(list)

for pointid, line in enumerate(lines):
    tmp=line.replace('position=<','').replace('> velocity=<',',').replace('>\n','')
    #print(len(tmp.split(',')))
    info = tmp.split(',')
    #print(tmp.split(','))
    posvel[pointid]=([float(info[0]),float(info[1]),float(info[2]),float(info[3])])

print(posvel)


def evolve(pointlist,stepsize):
    #for i in range(0,100*stepsize,stepsize):
    i=0
    #while i<300000:
    for i in range(10144-stepsize,10144+stepsize,1):
        print(i)
        #if i%1000==0:
            #print('plotting')
        plt.figure()
        for key,values in pointlist.items():
            #print(point)
            point= pointlist[key]
            plt.scatter(x=point[0]*(i*point[2]),y=(point[1]+(i*point[3])))
        plt.savefig('./plots/data_'+str(i).zfill(8)+'.png')


evolve(posvel,3)
exit()

import re
import numpy as np
from operator import itemgetter

e10 = [[int(z) for z in re.findall(r'-?\d+', x)] for x in lines]

n10 = np.array(e10)

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

def row_exists(coords):
    return len(set(np.array(sorted(coords, key=itemgetter(0)))[:6, 0])) == 1

for i in range(1, 20000):
    coords += vels
    if row_exists(coords):
        print(i)


import matplotlib.pyplot as plt

coords = n10[:, :2].copy()
vels = n10[:, 2:].copy()

coords += 10144*vels

canvas = np.zeros(coords.max(axis=0)+2)
canvas[coords[:, 0], coords[:, 1]] += 1


minx, miny = coords.min(axis=0)
plt.imshow(canvas[minx-1:, miny-1:].T)
plt.show()

