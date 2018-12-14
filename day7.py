import numpy as np
import networkx as nx

from collections import Counter

f = open("./input_7.txt",'r')
lines = f.readlines()

dependencies = {}
depcount = Counter()
graphnet = []

#networkx.DiGraph()
DG = nx.DiGraph()
allnodes = set()

for line in lines:
    #print(line)
    fromnode = (line.lower().split('step')[1].split(' ')[1])
    tonode = (line.lower().split('step')[2].split(' ')[1])
    allnodes.add(fromnode)
    allnodes.add(tonode)
    graphnet.append((fromnode,tonode))
    try:
        dependencies[fromnode].append(tonode)
    except:

        dependencies[fromnode] = []
        dependencies[fromnode].append(tonode)

    depcount[fromnode] += 1

    DG.add_edge(fromnode, tonode)



sp = nx.lexicographical_topological_sort(DG)
route=''.join(sp)
print(route)

offset = ord('a')-1
#part two, need to map the nodes, is there 5 branches of parallel work?


workers=5
pastnode=route[0]
cost=0
for r in route:
    for path in nx.all_simple_paths(DG, source=pastnode, target=r):
        print(path)
    #pastnode=r



lines= graphnet
steps = set([s[0] for s in lines] + [s[1] for s in lines])

def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]


t = 0
workers = [0 for _ in range(5)]
work = [None for _ in range(5)]
while steps or any(w > 0 for w in workers):
    cand = list(next_step(steps, lines))
    cand.sort()
    cand = cand[::-1]

    for i in range(5):
        workers[i] = max(workers[i] - 1, 0)
        if workers[i] == 0:
            if work[i] is not None:
                lines = [(a, b) for (a, b) in lines if a != work[i]]
            if cand:
                n = cand.pop()
                workers[i] = 60 + ord(n) - ord('a')
                work[i] = n
                steps.remove(n)

    t += 1

print(t)

