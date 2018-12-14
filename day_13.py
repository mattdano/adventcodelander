from collections import defaultdict
from itertools import cycle


f = open('./advent_code/input_13.txt','r')
lines = f.readlines()
mycarts = ['<','^','>','v']
lookup = {'<':-1,'^':-1j,'>':1,'v':-1j}
underneth = {"<": "-","^": "|",">": "-","v": "|"}
cart_position={}
cart_heading={}


cartnum=0
for y,line in enumerate(lines):
    for cart in mycarts:
        if cart in line:
            cart_pos = line.index(cart)
            #print(cart,cart_pos)
            x=cart_pos
            print(cart,x,y)
            cart_position[cartnum]=[x,y]
            cart_heading[cartnum]=cart
            #nextstep = lines[y][x]
            cartnum+=1

print(cart_position)
print(cart_heading)


tracks = defaultdict(str)
carts = []
for y, line in enumerate(lines):
    for x, l in enumerate(line):
        if l in mycarts:
            cartline = underneth[l]
        else:
            cartline = l
        if cartline in "\\/|+-":
            #store this bit. or can use numpy array maybe
            tracks[(x + y * 1j)] = cartline


trackturns = {}
carts = {}
lookup = {'<':-1,'^':-1j,'>':1,'v':-1j}
tracker = defaultdict(list)

for i, row in enumerate(lines):
    for j, c in enumerate(row.replace('\n','')):
        loc = j - i * 1j
        if c in r'/\+':
            trackturns[loc] = c
        elif c in lookup:
            carts[loc] = lookup[c], cycle([1j, 1, -1j])

counter=0
while len(carts) > 1:
    for loc in sorted(carts, key=lambda x: (-x.imag, x.real)):
        if loc not in carts:
            continue
        dxn, turn = carts.pop(loc)

        loc += dxn

        if loc in carts:
            print('Cart collision!', loc.real,loc.imag, '(cart', loc - dxn)
            del carts[loc]
            continue

        track = trackturns.get(loc)
        if track == '+':
            dxn = dxn * next(turn)
        elif track is not None:
            dxn *= 1j * (2 * ((track == '/') ^ (dxn.real == 0)) - 1)

        carts[loc] = dxn, turn
        tracker[counter].append(loc)
    counter+=1
print('Last cart standing',carts)


def draw_tracks(tracker=[]):
    import matplotlib.pyplot as plt
    import numpy as np
    grid = np.zeros((len(lines[0]),len(lines)))

    for t in tracks:
        x = int(np.real(t))
        y = int(np.imag(t))
        grid[x,y] = 1

    for step in range(0,len(tracker[0])-1):
        #step=0
        plt.figure(figsize=(10,10))
        plt.imshow(grid.T,interpolation=None,aspect='auto',cmap='Greys')
        for cartpos in tracker[step]:
            cx = int(cartpos.real)
            cy = -int(cartpos.imag)
            plt.scatter(cx,cy,c='red')
            plt.xlim((0, 140))
            plt.ylim((0, 140))
            plt.savefig('./advent_code/plots/carts_'+str(int(step)).zfill(4))

draw_tracks(tracker)
print(tracker[0][0])