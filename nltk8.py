#lemmatizing is kind of stemming but not exactly stemming, lemmatization may find out the synonym of the word.
#The goal of both stemming and lemmatization is to
#reduce inflectional forms and sometimes derivationally related forms of a word to a common base form
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# print lemmatizer.lemmatize("ephermal")
# print lemmatizer.lemmatize("cacti")
# print lemmatizer.lemmatize("geese")
# print lemmatizer.lemmatize("rocks")
# print lemmatizer.lemmatize("python")
# print lemmatizer.lemmatize("wolves")
# print lemmatizer.lemmatize("abaci")
# print lemmatizer.lemmatize("understood",)
print lemmatizer.lemmatize("better", pos="a")
print lemmatizer.lemmatize("run", 'v') #another way of writing a pos
#default pos-tag taken in the second argument is a noun "n"
