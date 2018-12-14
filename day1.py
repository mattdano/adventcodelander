import pandas as pd

f = open('./input_1.txt')
nums=[]
tally= 0
cumlist=[]
lines  = f.readlines()
#lines=['3','3','4','-2','-4']

print(len(lines))
def test():
    tally = 0
    cumlist = set()
    ncount=0
    while True:
        for num in lines:
            #nums.append(int(num))
            tally+=int(num)
            if tally in cumlist:
                print(tally)
                cumlist.add(tally)
                print(len(cumlist))
                print(cumlist)
                return ncount
            cumlist.add(tally)
        ncount=+1
print(test())

#freqs = pd.read_csv('./input_1.txt')
print(sum(nums))