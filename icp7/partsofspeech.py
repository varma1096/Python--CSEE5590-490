from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

input = open('input1.txt','r')
text = input.read()
words = word_tokenize(text)
print(ne_chunk(pos_tag(words)))