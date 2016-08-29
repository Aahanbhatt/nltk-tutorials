import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]
# documents = []
# for category in movie_reviews.categories():
#     for fileid in movie_reviews.fileids(category):
#         documents.append(list(movie_reviews.words(fileid, category))

random.shuffle(documents)   #to shuffle the data, because the movie_reviews are already trained once and we need random data

#print documents[1] it will print the first document review and will give the features/words. end of the list gives a pos or neg review

#In machine learning "features" are the units through which we train the algorithm.
#here the words are taken as features such that we can train Naive Bayes using the words for reviews
'''In text classification we will take each and every word of the review and we will find the most popular word,
    later we will find the negative/positive words from the most popular words and will reviews it as a whole'''

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)  #Frequency Distribution tells us the Frequency Distribution of each vocabulary item in the text.
#print all_words['war']  to print the Frequency of specific word in the text.
#print all_words.most_common(15)
