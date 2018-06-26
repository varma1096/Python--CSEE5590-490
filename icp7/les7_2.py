import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('wordnet')

with open(r'input1.txt', 'r') as file:
    for line in file:
        stokens = nltk.sent_tokenize(line)
        wtokens = nltk.word_tokenize(line)

        for s in stokens:
            print("Sentence Tokens: ",s)
        for t in wtokens:
            print("Word Tokens: ",t)