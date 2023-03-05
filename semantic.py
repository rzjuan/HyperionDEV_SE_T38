
#  NLP library is imported
import spacy

#  English NLP model is loaded into the nlp variable 
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana tiger')

#  Examine each of the tokens within the phrase
for token1 in tokens:
	for token2 in tokens:
		print(token1.text, token2.text, token1.similarity(token2))

"""
Note:

It is interesting how the NLP takes and assess different words 
considering what I believe are different criteria or at least it is 
what it seems. Monkey cat there is almost 60% of similarity as they are both
animals however, it is surprising that monkey tiger (new I added) has almost 65%
which might be because of the back they can live in the same habitat.
Monkey banana has also a high % considering the stereotype that monkey eats banana
but I am a bit intrigued about the fact dad the similarity between cat and tiguer
only ~57% being both from the same "type" and cat and monkey has ~60%
"""

