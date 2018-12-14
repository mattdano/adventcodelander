import numpy as np

f = open("./input_3.txt",'r')
claims = {}

fabric = np.zeros((1001,1001))
lines= f.readlines()
for line in lines:
    #print(line)
    splits = line.split(' ')

    id = splits[0]
    x,y = splits[2].replace(':','').split(',')
    x=int(x)
    y=int(y)
    width,height = splits[3].replace('\n','').split('x')
    width=int(width)
    height=int(height)

    #the actual mahts here.
    #rest is pointless

    fabric[x:x+width,y:y+height] += 1.0

    # end of useful

    #print(id,x,y,width,height)
    claims[id] = {}
    claims[id]['x']=x
    claims[id]['y']=y
    claims[id]['width']=width
    claims[id]['height']=height

print(np.sum(fabric>=2))

# round 2
#check the area == 1

for line in lines:
    #print(line)
    splits = line.split(' ')

    id = splits[0]
    x,y = splits[2].replace(':','').split(',')
    x=int(x)
    y=int(y)
    width,height = splits[3].replace('\n','').split('x')
    width=int(width)
    height=int(height)

    #the actual mahts here.
    #rest is pointless
    if np.sum(fabric[x:x+width,y:y+height]==1) == width*height:
        print(id,np.sum(fabric[x:x+width,y:y+height]==1) == width*height)


