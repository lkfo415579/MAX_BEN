from __future__ import division
import cPickle as pickle

def pre_recall(args):
	#pickle.dump( favorite_color, open( "class.p", "wb" ) )
	#classifier = pickle.load( open( "class.p", "rb" ) )
	#
	f_sets_file = args['f_sets_file']
	if f_sets_file != 'no':
		print '########Starting constructing new f_sets from '+f_sets_file+'#######'
		f_sets = pickle.load(open(f_sets_file,'rb'))
		print '########End of  constructing new f_sets from '+f_sets_file+'#######'
	else:
		f_sets = 'no'
	####
	class_file = args['class_file']
	if class_file != 'no':
		print '########Starting constructing new classifier from '+class_file+'#######'
		classifier = pickle.load(open(class_file,'rb'))
		print '########End of  constructing new classifier from '+class_file+'#######'
	else:
		classifier = 'no'
	#################
	
	return [classifier,f_sets]
	#import nltk

	#train = f_sets[3000:]
	#dev = f_sets[2000:3000]
	#test = f_sets[:2000]
'''
	def test_maxent(algorithm):
		end = ""
		print'%11s' % algorithm, end
		try:
			classifier = nltk.classify.MaxentClassifier.train(
							train, algorithm, trace=0, max_iter=1000)
		except Exception as e:
			print 'Error: %r' % e
			return
		
		print 'This is most informative table'
		print classifier.show_most_informative_features(10)
		
		print 'Accuracy',
		print nltk.classify.accuracy(classifier,test)
		
		return classifier
'''
'''
	def active_megam():
		if nltk.megam._megam_bin is None:
			nltk.config_megam('/home/db32555/MM/nltk/max/megam/megam-64.opt')

	active_megam()
'''
	#classifier = test_maxent('MEGAM')

def TFPN_TABLE(classifier,dev):
	errors = []
	all =[]
	for (f,tag) in dev:
		guess = classifier.classify(f)
		if  guess != tag:
			errors.append((tag,guess,f))
		all.append((tag,guess,f))

	positive = 'OK'
	negative = 'WRONG'
	
	tp = 0
	fp = 0
	fn = 0
	tn = 0
	
	for (tag,guess,f) in all:
		if tag == guess and tag == positive:
			tp += 1
		if tag != guess and tag == positive:
			fp += 1
		if tag != guess and tag == negative:
			fn += 1
		if tag == guess and tag == negative:
			tn += 1
			
	print ' '*21+'Correct'+' '*5 + 'In-correct'
	print 'Selected'+' '*9 + 'True Positive' + ' ' *5 + 'False Positive'
	print ' '*19 + str(tp) + ' '*12 + str(fp)
	print 'Not Selected'+' '*5 + 'False Negative' + ' ' *5 + 'True Negative'
	print ' '*19 + str(fn) + ' '*12 + str(tn)
	
	P = (tp/(tp+fp))*100
	R = (tp/(tp+fn))*100
	print 'Precision : ' + str("{0:.4f}".format(P))
	print 'Recall : ' + str("{0:.4f}".format(R))
	print 'F-Score : ' + str("{0:.4f}".format(2*P*R/(P+R)))
	print 'Accurancy : ' + str("{0:.4f}".format((tp+tn)*100/(fp+tn+tp+fp)))
	
	
	return errors

#errors = TFPN_TABLE(classifier,dev)
if __name__ == "__main__":
	pre_recall()

