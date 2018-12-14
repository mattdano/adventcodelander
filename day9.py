from collections import defaultdict, deque

players = 403
lastscore = 71920

players = 10
lastscore = 1618

players = 13
lastscore = 7999


hiscore = 8317

circlebuffer = [0,2,1]

pos = 1
abspos = 1
realpos=1
# [2]  0 (2) 1
# [3]  0  2  1 (3)
# [4]  0 (4) 2  1  3
# [5]  0  4  2 (5) 1  3
# [6]  0  4  2  5  1 (6) 3
# [7]  0  4  2  5  1  6  3 (7)
# [8]  0 (8) 4  2  5  1  6  3  7
# [9]  0  8  4 (9) 2  5  1  6

def marblegame(players,lastscore):
    #only works for some cases. not sure why
    currentpos = 1

    playerscores = defaultdict(int)
    balls= 3
    for i in range(3,lastscore+1):
    #while True:
        if i %23 ==0:
            playerscores[(i+2)%players] += i+circlebuffer[currentpos-7]
            #print('23+',circlebuffer[currentpos-7])
            circlebuffer.pop(currentpos-7)
            currentpos=currentpos-7
            #print(circlebuffer)
            #print('SPECIAL',i,circlebuffer[currentpos])

        else:
            #print(circlebuffer)
            currentpos=(currentpos+2)#%(len(circlebuffer))
            if currentpos > len(circlebuffer):
                currentpos-=len(circlebuffer)
            circlebuffer.insert(currentpos,i)
            #print(currentpos,len(circlebuffer))

    print(playerscores)
    print(max(playerscores.values()))

    return max(playerscores.values())


def marble_use_deque(players,lastscore):
    playerscores = defaultdict(int)
    circle = deque([0])
    for i in range(1,lastscore+1):
        if i %23 ==0:
            circle.rotate(7)
            playerscores[(i+2)%players] += i+circle.pop()
            circle.rotate(-1)
            #print(circlebuffer)
            #print('SPECIAL',i,circlebuffer[currentpos])
        else:
            circle.rotate(-1)
            circle.append(i)
            #print(circle)

    print(playerscores)
    print(max(playerscores.values()))

    return max(playerscores.values())

if __name__ == '__main__':
    marblegame(13,7999)
    marble_use_deque(13,7999)
    marblegame(403,71920)
    marble_use_deque(403,71920)
    marble_use_deque(403,71920*100)