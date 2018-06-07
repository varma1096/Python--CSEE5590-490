
i_f= open('input_file.txt','r')
o_f = open('output.txt' ,'w')
c = 1
line = i_f.readline()

while line != "":
    len(line)
    c = c+1
    line=line[:len(line)-1]
    print(line,len(line))

    o_f.write(line + " , " + str(len(line)) + "\n")
    line = i_f.readline()