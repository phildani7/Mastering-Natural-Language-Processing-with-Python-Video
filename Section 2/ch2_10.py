import nltk
corpus=u"<s> hello how are you doing ? Hope you find the book interesting. </s>".split()
sentence=u"<s>how are you doing</s>".split()
vocabulary=set(corpus)
print(len(vocabulary))
cfd = nltk.ConditionalFreqDist(nltk.bigrams(corpus))
print([cfd[a][b] for (a,b) in nltk.bigrams(sentence)])
print([cfd[a].N() for (a,b) in nltk.bigrams(sentence)])
print([cfd[a].freq(b) for (a,b) in nltk.bigrams(sentence)])
print([1 + cfd[a][b] for (a,b) in nltk.bigrams(sentence)])
print([len(vocabulary) + cfd[a].N() for (a,b) in nltk.bigrams(sentence)])
print([1.0 * (1+cfd[a][b]) / (len(vocabulary)+cfd[a].N()) for (a,b) in nltk.bigrams(sentence)])
cpd_mle = nltk.ConditionalProbDist(cfd, nltk.MLEProbDist, bins=len(vocabulary))
print([cpd_mle[a].prob(b) for (a,b) in nltk.bigrams(sentence)])
cpd_laplace = nltk.ConditionalProbDist(cfd, nltk.LaplaceProbDist, bins=len(vocabulary))
print([cpd_laplace[a].prob(b) for (a,b) in nltk.bigrams(sentence)])

