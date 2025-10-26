lines = ['one', 'two', 'three']
with open('file.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done! ')