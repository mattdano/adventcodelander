import pprint
from collections import defaultdict
import copy

f = open('input_16.txt','r')
lines = f.readlines()
breaker = 3259

def addr(register,a,b,c):
    register[c] = register[a]+register[b]
    return register

def addi(register,a,b,c):
    register[c] = register[a]+b
    return register

def mulr(register,a,b,c):
    register[c] = register[a]*register[b]
    return register

def muli(register,a,b,c):
    register[c] = register[a]*b
    return register

def banr(register,a,b,c):
    register[c] = register[a]&register[b]
    return register

def bani(register,a,b,c):
    register[c] = register[a]&b
    return register

def borr(register,a,b,c):
    register[c] = register[a]|register[b]
    return register

def bori(register,a,b,c):
    register[c] = register[a]|b
    return register

def setr(register,a,b,c):
    register[c] = register[a]
    return register

def seti(register,a,b,c):
    register[c] = a
    return register

def gtir(register,a,b,c):
    if a> register[b]:
        register[c] = 1
    else:
        register[c] = 0
    return register

def gtri(register,a,b,c):
    if register[a]> b:
        register[c] = 1
    else:
        register[c] = 0
    return register

def gtrr(register,a,b,c):
    if register[a]> register[b]:
        register[c] = 1
    else:
        register[c] = 0
    return register

def eqir(register,a,b,c):
    if a == register[b]:
        register[c] = 1
    else:
        register[c] = 0
    return register

def eqii(register,a,b,c):
    if b == register[a]:
        register[c] = 1
    else:
        register[c] = 0
    return register

def eqrr(register,a,b,c):
    if register[b] == register[a]:
        register[c] = 1
    else:
        register[c] = 0
    return register


opfuncts = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqii,eqrr]

score = defaultdict(int)


opcode_index = {}
counter = 0
score = defaultdict(int)
onlyop = {}
solutions = defaultdict(set)
for n in range(0,breaker,4):
    before = list(map(int,lines[n][9:-2].split(', ')))
    opcode = list(map(int,lines[n+1].replace('\n','').split(' ')))
    after = list(map(int,lines[n+2][9:-2].split(', ')))
    #print(before)
    #print(opcode)
    #print(after)
    opcode_index[counter] = opcode[0]
    ops = []
    solutions[counter] = set(opfuncts)
    for op in opfuncts:
        regcopy = copy.copy(before)
        simafter = op(regcopy,opcode[1],opcode[2],opcode[3])
        if after == simafter:
            score[counter]+=1
            onlyop[counter] = op
            ops.append(op)
    solutions[counter].intersection_update(ops)
    counter+=1

count = 0
for v in score.values():
    if v>2:
        count+=1
print(count)

mapping = {}

#print(score)
count = 0
for key , value in solutions.items():
    #print(key,len(value))
    if len(value)==1:
        mapping[opcode_index[key]] = value

    for opkey, opvalue in mapping.items():
        for okey, ovalue in solutions.items():
            if opvalue != ovalue:
                ovalue.difference_update(opvalue)


print(mapping)
myregister = [0,0,0,0]
for l in range(breaker+3,len(lines)):
    #print(lines[l][0:-1])
    #print(lines[l][0:-1].split(' '))
    #break
    gate = list(map(int,lines[l][0:-1].split(' ')))
    operation = list(mapping[gate[0]])[0]
    #print(operation[0])
    myregister = operation(myregister,gate[1],gate[2],gate[3])
    print(myregister)

print("-------")
print('On register one:',myregister[0])