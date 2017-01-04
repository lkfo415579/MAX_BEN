import nltk
nltk.usage(nltk.classify.ClassifierI)

train = [
(dict(a=1,b=1,c=1), 'y'),
(dict(a=1,b=1,c=1), 'x'),
(dict(a=1,b=1,c=0), 'y'),
(dict(a=0,b=1,c=1), 'x'),
(dict(a=0,b=1,c=1), 'y'),
(dict(a=0,b=0,c=1), 'y'),
(dict(a=0,b=1,c=0), 'x'),
(dict(a=0,b=0,c=0), 'x'),
(dict(a=0,b=1,c=1), 'y'),
]
test = [
(dict(a=1,b=0,c=1)), # unseen
(dict(a=1,b=0,c=0)), # unseen
(dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
(dict(a=0,b=1,c=0)), # seen 1 time, label=x
]

end=' '

def print_maxent_test_header():
	print(' '*11+''.join(['      test[%s]  ' % i
						  for i in range(len(test))]))
	print(' '*11+'     p(x)  p(y)'*len(test))
	print('-'*(11+15*len(test)))

def test_maxent(algorithm):
	print '%11s' % algorithm, end
	try:
		classifier = nltk.classify.MaxentClassifier.train(
						train, algorithm, trace=0, max_iter=1000)
	except Exception as e:
		print 'Error: %r' % e
		return

	for featureset in test:
		pdist = classifier.prob_classify(featureset)
		print '%8.2f%6.2f' % (pdist.prob('x'), pdist.prob('y')), end
	print()

print_maxent_test_header();
#test_maxent('GIS');
#test_maxent('IIS')
test_maxent('MEGAM')
#test_maxent('TADM')


