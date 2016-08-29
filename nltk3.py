'''stemming = it is a form of data processing, for example : take any word and identify or process the root stem.
    I'am riding a horse. Get rid of "ing" from riding make it "ride" as it will make it easier in text processing'''

# I was taking a ride in the care
# I was riding in the car

''' Often in large datasets, there will be many words and sentences which means the same, hence stemming is used to
    get rid of such same meaning words'''


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoning", "pythonista", "pythoned", "pythonly"]

# for w in example_words:
#     print ps.stem(w)

example_sentence = 'It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once.'

words = word_tokenize(example_sentence)
for w in words:
    print ps.stem(w)
