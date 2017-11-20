import random
with open('pendigits.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('pendigits_random.txt','w') as target:
    for _, line in data:
        target.write( line )