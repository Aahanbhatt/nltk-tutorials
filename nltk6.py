import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer  # unsupervised machine learning sentence tokenizer, we can train it if we want to .

#Here we are talking about chinking, which is breaking down of things or removal of something from chunking, eg: chunk this except this.

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkgram = r"""Chunk: {<.*>+}
                                }<VB.?|IN|DT>+{"""
            chunkParser = nltk.RegexpParser(chunkgram)
            chunked = chunkParser.parse(tagged)

            #print chunked

            chunked.draw()  #It will give the chunks in a tree format using matplotlib

    except Exception as e:
        print str(e)

process_content()
