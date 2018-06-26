import nltk
from nltk.stem import SnowballStemmer
input_data=open('input1.txt',"r")
data=input_data.read()
words = nltk.word_tokenize(data)
stemm=SnowballStemmer('english')
stem1= nltk.PorterStemmer()
for k in words:
  print("Stemmimg for word "+k+" is "+ stemm.stem(k))

for k in words:
    print("Stemmimg porte for word " + k + " is " + stem1.stem(k))