f = open('./input_12.txt')
lines = f.readlines()
init_state = lines[0].replace('initial state: ','')
init_state = '...#..#.#..##......###...###...........'
prefix=5
state = [0]*prefix

for i in init_state:
    if i =='#':
        state.append(1)
    else:
        state.append(0)
state += state + [0]*prefix*2

print(state)
exit()
#print(init_state)
#exit()
rules = dict()
for line in lines[2:]:
    tmp = line.replace('\n','')
    #print(tmp)
    ruleset = ''
    for i in tmp[0:5]:
        #print(i)
        if i == '#':
            ruleset+='1'
        else:
            ruleset+='0'
    if tmp[-1] == '#':
        outcome = 1
    else:
        outcome = 0

    rules[ruleset] = outcome

    #break

print(rules)
print(state)
def nextgen(in_gen):
    output = [0,0,0]
    for pot in range(3,len(in_gen)-3):
        #print(in_gen[pot-2:pot+3])
        check =''.join(map(str,in_gen[pot-2:pot+3]))
        output.append(rules[check])
    output.append(0)
    output.append(0)
    output.append(0)

    return output




for i in range(0,21):
    state = nextgen(state)
    print(state)

total = 0
for id ,i in enumerate(state):
    if i==1:
        total += id-3

print(total)