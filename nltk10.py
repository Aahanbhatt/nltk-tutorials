# wordnet is one of the largest corpora provided with nltk, we can lookup definitions, synonyms, etc.

from nltk.corpus import wordnet

syns = wordnet.synsets("program")

# print syns[0].lemmas()[0].name() #printing only the word
#
# print syns[0].name() #print the synonym synsets
#
# print syns[0].definition() #getting a definition of any word
#
# print syns[0].examples() #getting a sentece example

synonyms = []
antonyms = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

# print set(synonyms)
# print set(antonyms)

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')

print w1.wup_similarity(w2) #wup is wu-palmer similarity, it gives us a score on how similar two words are

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')

print w1.wup_similarity(w2)

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cycle.n.01')

print w1.wup_similarity(w2)
