input_string=input("Enter string:")
sp=[]
sp=input_string.split()
wordfreq=[sp.count(p) for p in sp]
print(dict(zip(sp,wordfreq)))