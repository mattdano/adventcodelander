import numpy as np
import datetime
import pandas as pd
f = open("./input_4.txt",'r')

twohour = np.zeros(120)
lines= f.readlines()
store = []
for line in lines:
    split = line.split(']')
    mydate =(split[0].replace('[',''))
    #print(mydate)
    parsed_date = datetime.datetime.strptime(mydate,'%Y-%m-%d %H:%M')
    print(split[1])
    store.append([parsed_date,split[1]])

    t=mydate.split(' ')[1].split(':')
    #print(t[0],t[1])
    if t[0] == '23':
        hour=0
    elif t[0] == '00':
        hour=1
    else:
        print(t[0])
    minute=int(t[1])
    #print(hour,minute)
    #twohour[hour*60]


sortedstore = sorted(store,key=lambda r: r[0])
print(sortedstore)

diary= dict()
timeline=dict()

minuteline = np.zeros(60)

for i in sortedstore:

    if 'Guard' in i[1]:
        currentguard=int(i[1].split('#')[1].split(' ')[0])
        #print(currentguard)

    if 'asleep' in i[1]:
        startsleep = i[0]

    if 'wakes' in i[1]:
        wakeup= i[0]
        slept=wakeup-startsleep
        try:
            diary[currentguard]  += slept.seconds
        except:
            diary[currentguard] = 0
            diary[currentguard] += slept.seconds

        print(startsleep.minute,wakeup.minute)

        try:
            timeline[currentguard][startsleep.minute:wakeup.minute] += 1
        except:
            timeline[currentguard] = np.zeros(60)
            timeline[currentguard][startsleep.minute:wakeup.minute] += 1

        print('Guard:',currentguard,slept.seconds)

most = 0

for key, value in diary.items():
    if value > most:
        most=value
        guard=key

print(guard,most/60)

print(timeline[guard])
print(timeline[guard].argmax())
print(timeline[guard].argmax()*guard)

mostest = 0

for g,v in timeline.items():
    if np.max(v) > mostest:
        mostest = np.max(v)
        bestminute = v.argmax()
        bestg = g

print(bestg,mostest)
print(timeline[509])
print(bestg*bestminute)


#print(store)
#dataset = pd.DataFrame(store,columns=['date','info'])
#pd.to_datetime(dataset['date'])
#dataset = dataset.sort_values(by=['date'], ascending=True)
#print(dataset.head(5))
