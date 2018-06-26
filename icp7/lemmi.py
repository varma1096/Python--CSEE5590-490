from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

input_data=open('input1.txt',"r+")
data=input_data.read()
words=word_tokenize(data)
for k in words:
    print("Lemmatizor for word "+k+" is "+WordNetLemmatizer().lemmatize(k))