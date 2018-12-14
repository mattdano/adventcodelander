from collections import defaultdict

f = open('./input_8.txt','r')
io = f.read()
#io = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
header = iter(map(int,io.replace('\n','').split(' ')))

def get_metadata(num_children, n_meta):
    if num_children == 0:
        return [sum(next(header) for _ in range(n_meta))] * 2

    meta, value = 0, 0
    value_children = defaultdict(int)

    for n in range(0,num_children):
        m, value_children[n] = get_metadata(next(header), next(header))
        meta += m


    for _ in range(n_meta):
        m = next(header)
        meta += m
        value += value_children[m - 1]

    return meta, value


meta, value = get_metadata(next(header), next(header))
print(meta,value)
