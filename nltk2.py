'''stop words are often left without any analysis because they may mean different at different situations, for example sarcasms.
    we don't care about the stop words. Most probable stop words would be "a", "an", "the", etc. '''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example sentence showing stopwords filtration."

stop_words = set(stopwords.words("english")) #list of stop words inbuilt in nltk

#print stop_words

words = word_tokenize(example_sentence)  #splitting the sentence by words

filtered_sentence = [w for w in words if not w in stop_words]

print filtered_sentence

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
# print filtered_sentence
