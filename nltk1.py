from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing = 1) word tokenizers and 2) sentence tokenizers
#corporas = body of text, ex: medical journals, research papers


example_text = 'hello there, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue, you should not eat fried food.'

#print(sent_tokenize(example_text)) #spliting the example_text by sentence

#print(word_tokenize(example_text)) #spliting the example_text by words

for i in word_tokenize(example_text):
    print i

# we can also split the sentence by using powerful regex and spliting by space, but nltk works more powerful
