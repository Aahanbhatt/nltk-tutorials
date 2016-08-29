# how to access corpus from nltk-data

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

samle = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(samle)

print tok[1:10]
