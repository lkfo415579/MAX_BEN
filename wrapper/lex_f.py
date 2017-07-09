#encoding=utf-8
#0000
#
def lex_f_main(args):
	##constants
	#lex_f = 'lex.e2f'
	#filename='zh2e',less_than=0.1
	lex_f = args['filename']
	less_than = args['less_than']
	order = args['order']
	symbol = args['symbol']
	chinese = args['chinese']
	#########
	#lex_dir = 'zh-en/'+lex_f
	lex_dir = lex_f
	print '#######This is reading '+lex_dir+' ##Pro < '+str(less_than)+'####'
	import sys
	#########
	from lex.readLexicalModelIntoDict_new import readLex
	#read Lex
	my_dict = readLex(lex_dir,order)

	def write_lex(ori,name,pro):
		#print '#####Writing Corpus into a file####'	
		file = open(filename, "a")

		pro = str(pro)
		
		file.write(str(ori +' '+ name +' ' + pro +'\n'))

		file.close()
		#print '#####Successfully Wrote into '+filename+'######'
	def filter(my_dict):
		#node,name,pro (0,1,2) in file
		from tool.check_digit_date import check_digit_date,check_chinese,check_symbol
		index = 0
		run = 0
		len_dict = len(my_dict)
		global cc_dict
		my_dict = dict(sorted(my_dict.iteritems(), key=lambda d:d[1], reverse = True))
		#my_dict = dict(sorted(my_dict.items(), key=lambda x:x[1]))
		cc_dict = my_dict
		
		for node in my_dict:
			#print '----------'
			run += 1
			#top
			top_count = 0
			#print my_dict[node]
			my_dict[node] = sorted(my_dict[node], key = lambda x : x[1],reverse = True)
			#s_dict = sorted(my_dict[node].iteritems(), key=lambda d:d[1], reverse = True)
			for cand in my_dict[node]:
				#print cand
				name = cand[0]
				pro = float(cand[1])
				key = True
				#print 'node (%s),name (%s) , pro (%.4f)' % (node,name,pro)
				if pro < less_than or pro == 1:
					key = False
					reason = 'Pro'
				if check_digit_date(node) or check_digit_date (name):
					#checked special case
					key = False
					reason = 'Special'
				if (check_symbol(node) or check_symbol(name)) and symbol:
					key = False
					reason = 'Symbol'
				if order == 'e2f':
					if chinese and check_chinese(name):
						#check english line contain chinese
						key = False
						reason = 'ZH_e2f'
				elif order == 'f2e':
					if chinese and check_chinese(name):
						#check english line contain chinese
						key = False
						reason = 'ZH_f2e'
				#################
				if key:
					if args['top']:
						top_count += 1
						if top_count == 11:
							break
					write_lex(node,name,pro)
				else:
					#print name
					progress = float(run) / float(len_dict)
					progress = str("{0:.2f}".format(progress*100))
					if index % 1000 == 0:
						#print 'numbers of deleted : ' + str(index)
						sys.stdout.write('Numbers of deleted(Reason : %-7s'% reason+') '+progress+'% : '  + str(index)+'\r')
						sys.stdout.flush()
					index += 1

	import os
	#directory = 'zh-en/'
	filename = lex_f+'_f'
	
	#if not os.path.exists(directory):
	#	os.makedirs(directory)
	if os.path.exists(filename):
		os.remove(filename)

	filter(my_dict)
	###
	sys.stdout.flush()
	print '\nDone!'


if __name__ == "__main__":
	default_lex = {'filename':'zh-en/zh2e','less_than':0.05,'order':'e2f','top':True}
	lex_f_main(default_lex)