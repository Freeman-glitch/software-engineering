with open("file.txt", 'a+') as f:
    f.write('\nIm additional line')

with open("file.txt", 'r') as f:
    result = f.readlines()
    print(result)