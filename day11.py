import numpy as np
import time
starttime = time.time()
#serial = 7511
serial = 7511

bestest = 0
largest=0
grid = np.zeros((300, 300))
for y in range(0,300):
    for x in range(0,300):
        rackid = x+10
        powerlevel = y*rackid
        powerlevel+=serial
        powerlevel*=rackid
        npower = int(str(int((powerlevel/100)))[-1])
        grid[x,y]= npower - 5


for y in range(0,300):
    for x in range(0,300):

        tmp = np.sum(np.sum(grid[x-1:x+2,y-1:y+2],axis=0))
        if tmp > largest:
            largest= tmp
            bestindx= [x-1,y-1]


print(largest)
print(bestindx)

def search_max_grid(power_array):
    maxp = 0
    maxl = 0, 0, 0

    for grids in range(1, 301):
        if not grids % 10:
            print("Now searching grid size", grids,"Max power so far", maxp)
        for r in range(300 - grids):
            for c in range(300 - grids):
                if np.sum(power_array[r:r+grids, c:c+grids]) > maxp:
                    maxp = np.sum(power_array[r:r+grids, c:c+grids])
                    maxl = r, c, grids
    print("Max powaaaaaah", maxp)
    print("Grid location", maxl)
    return maxl

search_max_grid(grid)

exit()
serial = int(7511)

def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5

grid = np.fromfunction(power, (300, 300))

print(np.sum(grid[236:249, 287:300]))
print(grid[234:234+13, 287:287+13].shape,np.sum(grid[235:235+13, 287:287+13]))
print(grid[234:234+13, 287:287+13].shape,np.sum(grid[235:235+13, 286:286+13]))
print(np.sum(grid[234:234+13, 287:287+13]))
print(grid[234:234+13, 287:287+13])
#exit()
largest = 0
for width in range(3, 18):
    windows = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = np.where(windows == maximum)
    #print(width, maximum, location[0][0] + 1, location[1][0] + 1)
    if maximum>=largest:
        largest = maximum
        bestcorner = [location[0][0] + 1, location[1][0] + 1,width]
        print(width, maximum, location[0][0] + 1, location[1][0] + 1,width)

print(largest)
print(bestcorner)
print('Time taken: ',time.time() - starttime)

#236,287,13
#236,287,13
# 135, 236, 287, 13
#234, 287, 13

#147 (234, 287, 13) 234,287,13

#234,287,13