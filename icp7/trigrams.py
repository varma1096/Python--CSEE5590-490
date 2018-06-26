from nltk.util import trigrams
from nltk.tokenize import word_tokenize
input=open('input1.txt','r')
line =input.read()
token= word_tokenize(line)
for x in trigrams(token):
    print(x)