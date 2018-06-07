with open("abc.txt" , 'r') as f:
    for line in f.readlines():
        words =len(line.split(' '))
        print(line,words)
