# encoding=utf-8
import nltk
nltk.usage(nltk.classify.ClassifierI)
import time
import sys
from lex.readLexicalModelIntoDict_set import readLex_set
import uniout
import unicodedata

def read_corpus(en_dir, zh_dir, tag):
	print 'Reading Corpus_%5s' % tag + ' :' + zh_dir + '  ' + en_dir + '...',
	en, zh = open(en_dir, 'r'), open(zh_dir, 'r')

	# local function for counting number of file lines
	def number_file(dir):
		with open(dir) as f:
			return sum(1 for _ in f)

	len_p = number_file(en_dir)

	corpus = []
	for x in range(0, len_p):
		en_words = []
		zh_words = []
		en_words = en.readline().split(" ")
		zh_words = zh.readline().split(" ")
		corpus.append([en_words, zh_words])
	print 'done'
	return corpus

def shuffle_corpus(corpus, method):
	import random
	len_corpus = len(corpus)
	print 'Starting shuffle corpus...',
	tmp = []
	for node in corpus:
		tmp.append(node[1])  # eng
	
	if method == 'random':
		random.shuffle(tmp) # random shuffle
	elif method == 'shift':
		tmp = tmp[len_corpus/20:] + tmp[:len_corpus/20] # shift 20%

	for index in range(0, len_corpus):
		corpus[index][1] = tmp[index]
	del tmp
		
	print 'done'
	return corpus

def prepare_lexical(my_dict, lex_table):
	lexical_file = lex_table
	print 'Reading Lexical Model into Dictionary :' + lexical_file + '...',
	order = 'e2f'
	my_dict = readLex_set(lexical_file, order)
	
	print 'done'
	return my_dict
''' # not used
def count_search_dict(word):
	#my_dict.get(word, 0)
	try:
		return len(my_dict[word])
		# return 0
	except KeyError:
		return 0
'''
# return 1 if dict[source] contains target
def count_match_dict(source, target):
	return 1 if target in set(my_dict.get(source, [])) else 0

def gender_features(en, zh):
	features = {}
	
	features["len_zh"] = float(len(zh))
	features["len_en"] = float(len(en))
	features["len_zh-en"] = float(len(zh) - len(en))
	features["len_en-zh"] = float(len(en) - len(zh))
	features["len_zh/en"] = float(float(len(zh)) / float(len(en)))
	features["len_en/zh"] = float(float(len(en)) / float(len(zh)))
	
	##LexicalModelDict##
	aligned_words = 0
	for word_zh in zh:
		match_count = 0
		for word_en in en:
			match_count += count_match_dict(word_zh, word_en)
		#features['num_match(%s)' % unicode(word_zh, 'utf-8')] = True if match_count > 0 else False #match_count
		##Dictionary-based features##
		##Word overlap ratio of S(T)
		if match_count > 0:
			aligned_words = aligned_words + 1
	
	#Number of aligned words:
	features['aligned_words'] = float(aligned_words)
	#Number of unaligned words
	features['unaligned_words_en'] = float(len(en) - aligned_words)
	features['unaligned_words_zh'] = float(len(zh) - aligned_words)
	##Word overlap ratio of S(T)
	features['ratio_overlap_en'] = float(float(aligned_words) / float(len(en)))
	features['ratio_overlap_zh'] = float(float(aligned_words) / float(len(zh)))
	
	##Matches Words_number##
	match_word = 0
	for word_zh in zh:
		for word_en in en:
			n_zh = unicodedata.normalize('NFKC', word_zh.decode('utf8'))
			n_en = unicodedata.normalize('NFKC', word_en.decode('utf8'))
			if n_zh == n_en:
				match_word += 1
				#features['match_word(%s)' % n_zh] = True
	features['match_word'] = float(match_word)

	#Longest aligned sequence of words
	#features['longest_ali_zh'] = logest_length(zh, features, "align")
	# Longest unaligned sequence of words
	#features['longest_unali_zh'] = logest_length(zh, features, "unalign")

	#Miscellaneous features
	#Numerical entities ratio
	zh_numerical = numerical(zh)
	en_numerical = numerical(en)
	try:
		features['numeri_ratio_zh/en'] = float(zh_numerical) / float(en_numerical)
	except ZeroDivisionError:
		features['numeri_ratio_zh/en'] = 0
	try:
		features['numeri_ratio_en/zh'] = float(en_numerical) / float(zh_numerical)
	except ZeroDivisionError:
		features['numeri_ratio_en/zh'] = 0

	#Punctuation ratio
	zh_num_pu = punctuation(zh)
	en_num_pu = punctuation(en)
	try:
		features['pun_ratio_zh/en'] = float(zh_num_pu) / float(en_num_pu)
	except ZeroDivisionError:
		features['pun_ratio_zh/en'] = 0
	try:
		features['pun_ratio_en/zh'] = float(en_num_pu) / float(zh_num_pu)
	except ZeroDivisionError:
		features['pun_ratio_en/zh'] = 0
	'''
	doc_words_en = set(en)
	doc_words_zh = set(zh)
	#run = 0
	
	w_list = []
	for word in word_features_en:
		if (word in doc_words_en): 
			for index in range(0, len(en)-1):
				if en[index] == word:
					w_list.append(word)
			#print 'removed ' + word
	w_list = list(set(w_list))
	#deletion
	for w in w_list:
		if en.count(w) > 0:
			en.remove(w)
	w_list = []
	for word in word_features_zh:
		if (word in doc_words_zh): 
			for index in range(0, len(zh)-1):
				if zh[index] == word:
					w_list.append(word)
			#print 'removed ' + word
	#w_list = list(set(w_list))
	#deletion
	for w in w_list:
		zh.remove(w)
		#print zh
	'''
	
	#contain script
	'''
	for word_zh in word_features_zh:
		features['contains(%s)' % word_zh] = (word_zh in doc_words_zh)
	'''
	
	'''
	if tmp_int == 0:
		features['num_match(%s)' % unicode(word_zh, 'utf-8')] = False
	else:
		features['num_match(%s)' % unicode(word_zh, 'utf-8')] = True
	'''
	
	# Unknown Words###can't find in lexical table
	'''
	tmp_int = 0
	for word_zh in zh:
		if count_search_dict(word_zh) == 0:
			tmp_int += 1
	features['unknown_word'] = tmp_int
	'''

	#print features
	#sys.exit()
	#print "%%%CORE"""
	#print features
	#print "%%%CORE"""
	return features

# return the count for how many digit in input
def numerical(input):
	return len([True for w in input if w.isdigit()])

# return the count for how many !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ in input 
def punctuation(input):
	import string
	return len([True for w in input if w in string.punctuation])

def logest_length(input, features, option):
	max_sequence, tmp_sequence = 0, 0
	for word in input:
		if option == 'align':
			tmp_sequence = tmp_sequence + 1 if (features['num_match(%s)' % unicode(word, 'utf-8')] > 1) else 0
		elif option == 'unalign':
			tmp_sequence = tmp_sequence + 1 if (features['num_match(%s)' % unicode(word, 'utf-8')] == 0) else 0
		if tmp_sequence > max_sequence:
			max_sequence = tmp_sequence
	return max_sequence

def append_features(corpus, tag, q, long, pid, info):
	if not info:
		print '\r###Appending features Tag : %5s' % tag + '#####PID : %2d' % (pid) + '###########           \r'
	run = 0
	len_all = len(corpus)
	featuresets = []
	print len(corpus)
	for (zh, en) in corpus:
		if run % 100 == 0:
			tmp_per = float(float(run) / float(len_all)) * 100
			percent = "{0:.2f}".format(tmp_per)
			sys.stdout.write('\r'+' ' * int(long * 1.7) + '-PID:%2d' % (pid) +
							 '-Line(%5s):' % tag + str(run) + '-' + str(percent) + '%           \r')
			sys.stdout.flush()
			# print '-Line('+tag+'):' + str(run) + '-',
		run = run + 1
		featuresets.append([gender_features(zh, en), tag])
	q.put(featuresets)
	
	if not info:
		print '\r###End of features Tag : %5s' % tag + '#####PID : %2d' % (pid) + '###########              \r'

def split_list(alist, wanted_parts=1, mode="equal_word"):
	result = []
	if mode == 'equal_word':
		# update this mode at 2017-01-06 
		total_size = 0
		total_size += sum([len(line[0]) + len(line[1]) for line in alist])
		each_size = total_size / wanted_parts
		current_count = 0
		tmp_result = []
		for line in alist:
			if current_count > each_size:
				result.append(tmp_result)
				current_count = 0
				tmp_result = []
			current_count += len(line[0]) + len(line[1])
			tmp_result.append(line)
		if len(tmp_result) > 0:
			result.append(tmp_result)

	else:
		length = len(alist)
		result = [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts] for i in range(wanted_parts)]
	return result

def muti_feat_adder(cores=2, c_l=[], info=False):
	import multiprocessing
	from multiprocessing import Process, Queue
	long = 0
	featuresets, q_list, corpus_list, jobs = [], [], [], []

	if cores % 2 != 0:
		print 'number of Cores must be even'
		return

	if not info:
		print '###Mutiprocessing cores = ' + str(cores) + '###'
		
	if len(c_l) != 1:
		numOfcuts = cores / 2
	else:
		numOfcuts = cores

	for corpus in c_l:
		for each in split_list(corpus[0], numOfcuts, "equal_word"):
			corpus_list.append([each, corpus[1]])

	
	#check lines of corpus
	if len(corpus_list) < cores:
		cores = len(corpus_list)
	# single corpus
	for x in range(1, cores + 1):
		tmp_q = Queue()
		q_list.append(tmp_q)
		
		tmp_p = multiprocessing.Process(target=append_features, args=(
			corpus_list[x - 1][0], corpus_list[x - 1][1], tmp_q, long, x, info))
		long += 20
		if long > 20:
			# print '#######'
			long = 0
		jobs.append(tmp_p)
		tmp_p.daemon = False
		tmp_p.start()
	
	index = 1
	for q in q_list:
		sys.stdout.write('\r-F_ID:%d-' % index + '\r')
		sys.stdout.flush()
		featuresets += q.get()
		del q
		index += 1
	for p in jobs:
		p.join()
		del p
	print '##End of merging featureset##'
	return featuresets

def check_count(feat, tag):
	total = len([True for node in feat if node[1] == tag])
	print 'Total [' + tag + '] : ' + str(total)

def test_maxent(algorithm, train_set, test_set):
	print "XXXXXXFeaturest DISPLAYXXXXXXX"
	print "F_LEN:%d" % len(train_set)
	print train_set[0]
	print "XXXXXXFeaturest DISPLAYXXXXXXX"
	####
	start_time = time.time()
	active_megam()
	print'%11s' % algorithm
	try:
		classifier
	except NameError:
		c_ex = True
	else:
		del classifier
	# try:
	feature_encoding = nltk.classify.maxent.TypedMaxentFeatureEncoding.train(train_set)
	classifier = nltk.classify.MaxentClassifier.train(train_set, algorithm, trace=1, max_iter=2000,encoding=feature_encoding,bernoulli=False)
	# except Exception as e:
		# print 'Error: %r' % e
		# return

	print 'This is most informative table\n', classifier.show_most_informative_features(20)
	print 'Length of Testset :%d' % len(test_set)
	print 'Accuracy : ', nltk.classify.accuracy(classifier, test_set) * 100, '%'
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))
	
	return classifier

def active_megam():
	if nltk.megam._megam_bin is None:
		import os
		path = os.getcwd()
		nltk.config_megam(path+'/megam/megam-64.opt')

def corpus2():
	# corpus 2
	zh_dir_2 = 'zh-en/1m_uni.tok.zh'
	en_dir_2 = 'zh-en/1m_uni.tok.en'

	corpus_ok = read_corpus(en_dir_2, zh_dir_2, 'OK')
	corpus_wrong = read_corpus(en_dir_2, zh_dir_2, 'WRONG')
	corpus_wrong = shuffle_corpus(corpus_wrong, 'random')
	print '###Generating featuresets ctb###'
	n_c_l = [[corpus_ok, "OK"], [corpus_wrong, "WRONG"]]
	
	n_cores = int(args['cores'])
	
	f_ctb = muti_feat_adder(n_cores, n_c_l)
	random.shuffle(f_ctb)
	test_ctb = f_ctb  # all

	print 'Accuracy',
	print nltk.classify.accuracy(classifier, test_ctb)

def sep_test_3(f_all, ratio_f_len):
	print 'Test_size : %.2f' % (ratio_f_len * 100) + '%'
	#ratio_f_len = float(args['len_test_sets'])
	f_l_mid = int(len(f_all) * (ratio_f_len/3))
	f_l_end = len(f_all) - f_l_mid
	center = len(f_all) / 2
	test_ctb = f_all[:f_l_mid]
	test_ctb += f_all[center-f_l_mid/2:center+f_l_mid/2]
	test_ctb += f_all[f_l_end:]
	print 'Len of Test : %d ' % len(test_ctb)
	return test_ctb

def find_wrong(args, classifier):
	start_time = time.time()
	# corpus um
	print '####Function find_wrong####'
	zh_dir_2 = args['zh_dir']
	en_dir_2 = args['en_dir']
	output_file = args['output']
	output_file_tu = output_file + '.wrong'
	output_file_ta = output_file + '.ok'
	output_file_tm = output_file + '.mid'
	print '####OutputFile: wrong='+output_file_tu+' ok='+output_file_ta+'####'

	corpus_ok = read_corpus(en_dir_2, zh_dir_2, 'OK')
	n_c_l = [[corpus_ok, "OK"]]
	
	if args['targetfile_t_origin'] != "":
		try:
			ori_corpus = read_corpus(args['targetfile_t_origin'], args['sourcefile_t_origin'], "original")
		except:
			ori_corpus = corpus_ok
	else:
		ori_corpus = corpus_ok
	
	print '###Generating featuresets ctb###'
	
	n_cores = int(args['cores'])
	
	##lexical model
	global my_dict
	try:
		if my_dict is None:
			tmp_void = True
	except NameError:
		my_dict = []
		my_dict = prepare_lexical(my_dict, args['lex_table'])
	
	f_all = muti_feat_adder(n_cores, n_c_l, False)
	
	#seaprate testset to 3 parts from total corpus
	test_ctb = sep_test_3(f_all, args['len_test_sets'])
	
	print '###Staring calculate accuracy###'
	print 'Accuracy : ', nltk.classify.accuracy(classifier, test_ctb) * 100, '%'
	print '###Finding Wrong & OK lines###'

	# preparefile
	#f = open('error/' + output_file + '_er', 'w')
	f_tu = open(output_file_tu, 'w')
	f_ta = open(output_file_ta, 'w')
	f_tm = open(output_file_tm, 'w')

	num_wrong = 0
	num_ok = 0
	num_mid = 0
	wrong_rate = float(args['wrong_rate'])
	ok_rate = float(args['ok_rate'])
	#
	run = 0
	for index in range(0, len(f_all)):
	
		if run % 100 == 0:
			tmp_per = float(float(run) / float(len(f_all))) * 100
			percent = "{0:.2f}".format(tmp_per)
			# sys.stdout.write('\n\r' * pid)
			# sys.stdout.flush()
			sys.stdout.write('\r'+'-Line(%5s):' %  str(run) + '-' + str(percent) + '%           \r')
			sys.stdout.flush()
			# print '-Line('+tag+'):' + str(run) + '-',
		run = run + 1
	
		##
	
		pdist = classifier.prob_classify(f_all[index][0])
		ok = float(pdist.prob('OK'))
		wrong = float(pdist.prob('WRONG'))
		if wrong >= wrong_rate:
			# print 'OK : ' + "{0:.3f}%".format(ok)
			# print 'WRONG : ' + "{0:.3f}%".format(wrong)
			# print 'Line : ' + str(index)
#			f_tu.write('OK : ' + "{0:.3f}%".format(ok * 100) + '\n')
#			f_tu.write('WRONG : ' + "{0:.3f}%".format(wrong * 100) + '\n')
#			f_tu.write('Line : ' + str(index+1) + '\n')
#			f_tu.write('Zh : '+ ' '.join(map(str, ori_corpus[index][1])))
#			f_tu.write('En : '+ ' '.join(map(str, ori_corpus[index][0])))
#			f_tu.write('--------------\n')
			f_tu.write(' ||| '.join([str(index+1), "{0:.3f}%".format(ok*100), "{0:.3f}%".format(wrong*100), ' '.join(map(str, ori_corpus[index][1])).strip(),  ' '.join(map(str, ori_corpus[index][0])).strip()]) + '\n')
			num_wrong += 1
		if ok >= ok_rate:
#			f_ta.write('OK : ' + "{0:.3f}%".format(ok * 100) + '\n')
#			f_ta.write('WRONG : ' + "{0:.3f}%".format(wrong * 100) + '\n')
#			f_ta.write('Line : ' + str(index+1) + '\n')
	#		f_ta.write('Zh : '+ ' '.join(map(str, ori_corpus[index][1])))
	#		f_ta.write('En : '+ ' '.join(map(str, ori_corpus[index][0])))
	#		f_ta.write('--------------\n')
			f_ta.write(' ||| '.join([str(index+1), "{0:.3f}%".format(ok*100), "{0:.3f}%".format(wrong*100), ' '.join(map(str, ori_corpus[index][1])).strip(),  ' '.join(map(str, ori_corpus[index][0])).strip()]) + '\n')
			num_ok += 1
		if wrong < wrong_rate and ok < ok_rate:
	#		f_tm.write('OK : ' + "{0:.3f}%".format(ok * 100) + '\n')
	#		f_tm.write('WRONG : ' + "{0:.3f}%".format(wrong * 100) + '\n')
	#		f_tm.write('Line : ' + str(index+1) + '\n')
	#		f_tm.write('Zh : '+ ' '.join(map(str, ori_corpus[index][1])))
	#		f_tm.write('En : '+ ' '.join(map(str, ori_corpus[index][0])))
	#		f_tm.write('--------------\n')
			f_tm.write(' ||| '.join([str(index+1), "{0:.3f}%".format(ok*100), "{0:.3f}%".format(wrong*100), ' '.join(map(str, ori_corpus[index][1])).strip(),  ' '.join(map(str, ori_corpus[index][0])).strip()]) + '\n')
			num_mid += 1
			
	print '\r',
	print 'Amount of wrong : ' + str(num_wrong)
	f_tu.write('Amount of wrong : ' + str(num_wrong))
	f_tu.close()

	print 'Amount of ok : ' + str(num_ok)
	f_ta.write('Amount of ok : ' + str(num_ok))
	f_ta.close()
	
	print 'Amount of mid : ' + str(num_mid)
	f_tm.write('Amount of mid : ' + str(num_mid))
	f_tm.close()
	
	print 'Total of lines : ' + str(len(f_all))
	
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))
	return f_all

def sort_corpus(corpus):
	print '########Starting sort_corpus#######'
	tmp = []
	for node in corpus:
		tmp.append(node[1])  # eng
	tmp.sort(key=lambda item: (-len(item), item), reverse=True)
	
	tmp_zh = []
	for node in corpus:
		tmp_zh.append(node[0])  # zh
	tmp_zh.sort(key=lambda item: (-len(item), item), reverse=True)
	##
	len_corpus = len(corpus)
	for index in range(0, len_corpus):
		corpus[index][1] = tmp[index]
		corpus[index][0] = tmp_zh[index]
	del tmp
	del tmp_zh
	print '########End of sort_corpus#######'
	return corpus
	
def print_corpus(corpus, postfix):
	full_name_zh = 'debug/hikari_zh'
	full_name_en = 'debug/hikari_en'
	f_zh = open(full_name_zh, 'w')
	f_en = open(full_name_en, 'w')
	for node in corpus:
		f_zh.write(' '.join(map(str, node[1])) + postfix)
		f_en.write(' '.join(map(str, node[0])) + postfix)
	f_en.close()
	f_zh.close()
	
def find_match(args, classifier):
	start_time = time.time()
	# find_match
	print '####Function find_match####'
	zh_dir_2 = args['zh_dir']
	en_dir_2 = args['en_dir']
	output_file = args['output']
	print '####OutputFile='+output_file+'####'
	corpus_ok = read_corpus(en_dir_2, zh_dir_2, 'OK')
	#corpus_ok = shuffle_corpus(corpus_ok, 'random')
	sort = args['sort']
	if sort:
		corpus_ok = sort_corpus(corpus_ok);
	
	#for debug use only
	print_corpus(corpus_ok, '')
	#####
	print '###Generating Windowsize corpus###'
	
	corpus_size = len(corpus_ok)
	windows_size = int(float(args['win_size'] * corpus_size))#5% of corpus as windows_size
	##
	print '###Windows Size : %d###' % windows_size
	
	real_corpus = []
	info_space = []
	
	tmp_info = 0
	for index in range(0, corpus_size):
		#record ori zh line
		zh_ori_line = []
		#got index then search
		#add original line
		tmp_info += 1
		real_corpus.append([corpus_ok[index][0], corpus_ok[index][1]])
		
		zh_ori_line.append(index)
		for x in range(1, windows_size):
			front = index - x
			next = index + x
			if front > 0:
				tmp_info += 1
				real_corpus.append([corpus_ok[index][0], corpus_ok[front][1]])
				zh_ori_line.append(front)
			if next < corpus_size:
				tmp_info += 1
				real_corpus.append([corpus_ok[index][0], corpus_ok[next][1]])
				zh_ori_line.append(next)
		info_space.append([tmp_info, index, zh_ori_line])
		tmp_info = 0
	
	#generate print corpus for display original corpus
	if args['targetfile_t_origin'] != "":
		try:
			ori_corpus = read_corpus(args['targetfile_t_origin'], args['sourcefile_t_origin'], "original")
		except:
			ori_corpus = real_corpus
	else:
		ori_corpus = real_corpus
	
	n_c_l = [[real_corpus, "OK"]]
	
	print '###Generating featuresets ctb###'
	
	n_cores = int(args['cores'])
	
	##lexical model
	global my_dict
	try:
		if my_dict is None:
			tmp_void = True
	except NameError:
		my_dict = []
		my_dict = prepare_lexical(my_dict, args['lex_table'])
	
	f_all = muti_feat_adder(n_cores, n_c_l, False)
	
	#'delete all tager'
	test_ctb = f_all  # all
	print 'Accuracy(one to one) : ', nltk.classify.accuracy(classifier, test_ctb) * 100, '%'

	f = open(output_file, 'w')
	num_match = 0
	ok_rate = float(args['ok_rate'])
	corpus_size = len(f_all)
	#windows_size = int(float(args['win_size'] * corpus_size))#5% of corpus as windows_size
	##
	print '####Starting search the highest OK lines####'
	run = 0
	
	try:
		#print wish_list
		wish_list.clear()
	except UnboundLocalError:
		wish_list = dict()

	cur_count = 0
	for index in range(0, corpus_size):
		#got index then search
		now_count = info_space[0][0]-1
		if cur_count == now_count:
			info_space.remove(info_space[0])
			cur_count = 0
			change = True
			run += 1
		else:
			change = False
			cur_count += 1

		if change:
			if wish_list:
				try:
					h_index = max(wish_list.iterkeys(), key=(lambda k: wish_list[k][0]))
					zh_line = info_space[0][2][wish_list[h_index][1]]
				except:
					break
				f.write('OK : ' + "{0:.3f}%".format(wish_list[h_index][0]) + '\n')
				f.write('WRONG : ' + "{0:.3f}%".format(1-wish_list[h_index][0]) + '\n')
				f.write('Line(zh) : ' + str(zh_line) + '\n')
				f.write('Line(en) : ' + str(info_space[0][1]) + '\n')
				f.write('zh : '+ ' '.join(map(str, real_corpus[h_index][1])))
				f.write('en : '+ ' '.join(map(str, real_corpus[h_index][0])))
				f.write('--------------\n')
				num_match += 1
				wish_list.clear()
				change = False
		else:
			pdist = classifier.prob_classify(f_all[index][0])
			ok = float(pdist.prob('OK'))
			wrong = float(pdist.prob('WRONG'))
			if ok >= ok_rate:
				offset = cur_count - 1
				wish_list.update({index: [ok, offset]})

	print 'Amount of match : ' + str(num_match)
	f.write('Amount of match : ' + str(num_match))
	f.close()
	
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))

def prepare_fset(args):
	import random
	global my_dict
	
	start_time = time.time()
	#####Reading Corpus From file#########
	zh_dir = args['zh_dir']
	en_dir = args['en_dir']
	
	corpus_ok = read_corpus(en_dir, zh_dir, "OK")
	corpus_wrong = read_corpus(en_dir, zh_dir, 'WRONG')
	corpus_wrong = shuffle_corpus(corpus_wrong, 'shift')
	
	###############################
	#0 is zh , 1 is en
	####feature############
	# config
	freq_weight = 0.1
	my_dict = []
	my_dict = prepare_lexical(my_dict, args['lex_table'])
	################################

	featuresets = []
	
	c_l = [[corpus_ok, "OK"], [corpus_wrong, "WRONG"]]
	#c_l = [[corpus_ok, "OK"]]

	n_cores = int(args['cores'])
	featuresets = muti_feat_adder(n_cores, c_l)
	#print "featFFFFF:%d" % len(featuresets)
	random.shuffle(featuresets)
	#featuresets = [(gender_features(zh, en), "OK") for (zh, en) in corpus]
	featuresets_len = len(featuresets)
	ratio_f_len = float(args['len_test_sets'])
	#f_len = int(featuresets_len * ratio_f_len)
	#devtest = featuresets[1000:2000]
	#train = featuresets[f_len:]
	#test = featuresets[:f_len]
	print "test_rate,Len Of featurests:%s" % args['len_test_sets']," ",featuresets_len
	test_len = int(float(featuresets_len) * ratio_f_len)
	#test_len = int(test_len)
	#print "LEN:%d" % test_len
	train, test = [], []
	extract_test_distinct = float(float(featuresets_len / test_len))
	current_sum = 0.0
	next_extract = extract_test_distinct
	for i in range(featuresets_len):
		current_sum += 1
		if current_sum >= next_extract:
			next_extract += extract_test_distinct
			test.append(featuresets[i])
		else:
			train.append(featuresets[i])
	print 'extract_test_distinct =', extract_test_distinct
	print 'train size = %d, test size = %d' % (len(train), len(test))

	######User Area#########
	
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))
	
	parameters = args

	####frequest words####
	'''
	#####
	print '###Generating frequest words ###'

	words_en = []
	words_zh = []
	for node in corpus_ok:
		for a in node[0]:
			words_en.append(a)
		for b in node[1]:
			words_zh.append(b)

	all_words_en = nltk.FreqDist(w.lower() for w in words_en)
	all_words_zh = nltk.FreqDist(c for c in words_zh)

	word_features_en = list(sorted(all_words_en, key=all_words_en.__getitem__, reverse=True))
	word_features_zh = list(sorted(all_words_zh, key=all_words_zh.__getitem__, reverse=True))

	word_features_en = word_features_en[:50]
	word_features_zh = word_features_zh[:50]
	#word_features_en = sorted(all_words_en)[:int(len(all_words_en) * freq_weight)]
	#word_features_zh = sorted(all_words_zh)[:int(len(all_words_zh) * freq_weight)]
	'''
	######################
	'''prepare_lexical'''
	
	return [featuresets, train, test, parameters]


def find_single_match(corpus, args, f, classifier):
	print_corpus(corpus, '\n')
	print '###Generating Windowsize corpus###'
	corpus_size = len(corpus)
	original_index = corpus
	real_corpus = []
	num_blank = 0
	
	#reading original source, target files
	if args['targetfile_t_origin'] != "":
		try:
			ori_corpus = read_corpus(args['targetfile_t_origin'], args['sourcefile_t_origin'], "original")
		except:
			ori_corpus = real_corpus
	else:
		ori_corpus = real_corpus
	
	for index in range(0, corpus_size):
		if corpus[index][1][0] == '[blankspace]':
			num_blank += 1
		for x in range(0, corpus_size):
			real_corpus.append([corpus[index][0], corpus[x][1]])
	
	print '###Generating featuresets ctb###'
	#input corpus
	n_c_l = [[real_corpus, "OK"]]
	#
	n_cores = int(args['cores'])
	
	##lexical model
	global my_dict
	try:
		if my_dict is None:
			tmp_void = True
	except NameError:
		my_dict = []
		my_dict = prepare_lexical(my_dict, args['lex_table'])
	###
	f_all = muti_feat_adder(n_cores, n_c_l, True)
	test_ctb = f_all
	print 'Accuracy(one to one) : ',
	print nltk.classify.accuracy(classifier, test_ctb) * 100,
	print '%'
	############
	
	num_match = 0
	ok_rate = float(args['ok_rate'])
	f_size = len(f_all)
	print '####Starting search the highest OK lines####'
	run = 0
	
	#create wish_list,
	try:
		wish_list.clear()
	except UnboundLocalError:
		wish_list = dict()
	
	
	now_index = 0
	for index in range(0, f_size):
		if index % corpus_size == 0:
			if wish_list:
				# finish searching retrieve the highest matched line
				try:
					h_index = max(wish_list.iterkeys(), key=(lambda k: wish_list[k][0]))
				except:
					break
				
				if args['sort']:
					zh_line = (h_index % corpus_size) - num_blank
					en_line = now_index
				else:
					zh_line = (h_index % corpus_size)
					en_line = now_index - 1
					
				f.write('OK : ' + "{0:.3f}%".format(wish_list[h_index][0] * 100) + '\n')
				f.write('WRONG : ' + "{0:.3f}%".format((1-wish_list[h_index][0]) * 100) + '\n')
				f.write('Line(zh) : ' + str(zh_line) + '\n')
				f.write('Line(en) : ' + str(en_line) + '\n')
				f.write('Zh : '+ ' '.join(map(str, ori_corpus[h_index][1])) + '\n')
				f.write('En : '+ ' '.join(map(str, ori_corpus[h_index][0])) + '\n')
				f.write('--------------\n')
				num_match += 1
				wish_list.clear()
			#
			now_index += 1
		else:
			#print f_all[index]
			pdist = classifier.prob_classify(f_all[index][0])
			ok = float(pdist.prob('OK'))
			wrong = float(pdist.prob('WRONG'))
			if ok >= ok_rate:
				wish_list.update({index: [ok]})

	print 'Amount of match : ' + str(num_match) +'\n--------------\n'
	f.write('Amount of match : ' + str(num_match)+'\n--------------\n')
	
	global total_match
	total_match += num_match
	
def RE_search(file_name):
	import re, mmap
	phrase = '<doc.*?>([\S\s]+?)<\/doc>'

	with open(file_name, 'r+') as f:
		data = mmap.mmap(f.fileno(), 0)
		mo = re.findall(phrase, data)
		
		if mo:
			#content = mo.group()
			content = mo
	try:
		return content
	except:
		return False
	#search all pages in one single doc

def read_corpus_str(str_en, str_zh):
	str_en = str_en.splitlines()
	str_zh = str_zh.splitlines()
	
	len_p_en = len(str_en)
	len_p_zh = len(str_zh)

	print 'English lines(%d)' % len_p_en
	print 'Chinese lines(%d)' % len_p_zh
	
	if len_p_en < len_p_zh:
		len_p = len_p_zh
	else:
		len_p = len_p_en
	
	corpus = []
	for x in range(0, len_p):
		en_words = []
		zh_words = []
		if x < len_p_en:
			en_words = str_en[x].split(" ")
		else:
			en_words = ["[blankspace]"]
		if x < len_p_zh:
			zh_words = str_zh[x].split(" ")
		else:
			zh_words = ["[blankspace]"]
		corpus.append([en_words, zh_words])
	return corpus
	
def process_xml_corpus(en_dir, zh_dir, args, full_name, classifier):
	global total_match
	sort = args['sort']
	f = open(full_name, 'wa')

	docs_en = RE_search(en_dir)
	docs_zh = RE_search(zh_dir)
	l_docs = len(docs_zh) - 1
	print 'Total wiki pages : %d ' % l_docs
	
	doc_id = 0
	total_match = 0
	for x in range(0, l_docs):
		try:
			corpus_ok = read_corpus_str(docs_en[x], docs_zh[x])
		except:
			pass
			
		if sort:
			corpus_ok = sort_corpus(corpus_ok);
		find_single_match(corpus_ok, args, f, classifier)
		
		doc_id += 1
		print '------------------'
		print 'DocID:%d' % doc_id
		print '@@@@Finished Reading a Doc@@@@'
		print '------------------'
		f.write('------------------')
		f.write('DocID:%d' % doc_id)
		f.write('------------------\n')
	
	print 'Total of match : ' + str(total_match) +'\n--------------\n'
	f.write('Total of match : ' + str(total_match)+'\n--------------\n')
	
	f.close()
	
def find_wiki_match(args, classifier):
	print '####Function find_match####'
	start_time = time.time()
	zh_dir = args['zh_dir']
	en_dir = args['en_dir']
	output_file = args['output']
	print '####OutputFile='+output_file+'####'
	process_xml_corpus(en_dir, zh_dir, args, output_file, classifier)
	print("---Total Used : %s Seconds ---" % (time.time() - start_time))

