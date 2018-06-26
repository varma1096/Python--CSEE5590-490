from nltk import pos_tag,ne_chunk,wordpunct_tokenize
file1=open('input1.txt','r')
text =file1.readline()
while text!='':
 print(ne_chunk(pos_tag(wordpunct_tokenize(text))))
 text=file1.readline()