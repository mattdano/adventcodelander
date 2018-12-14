from collections import Counter

f = open("./input_2.txt",'r')
lines = f.readlines()

store= []
for l in lines:
    store.append(l.replace('\n',''))

import editdistance

lowest = 50
for a in store:
    for l in store:
        distance = editdistance.eval(a,l)
        if distance!=0:
           if distance<lowest:
               lowest=distance
        if distance==1:
            print(a,l)
print(lowest)

atest='ivjhcadokesltwgsfsmqwrbnuy'
btest='ivjhcadokexltwgsfsmqwrbnuy'


exit()

mycounters = []
for l in lines:
    chars = l.replace('\n','')
    alphas= []
    for c in chars:
        alphas.append(c)
    c1 = Counter(chars)
    #print(c1)
    mycounters.append(c1)

threetally = 0
twotally = 0

for cnter in mycounters:
    #print(cnter.values())

    if 2 in cnter.values():
        twotally+=1

    if 3 in cnter.values():
        threetally+=1

print(threetally,twotally)
print(threetally*twotally)