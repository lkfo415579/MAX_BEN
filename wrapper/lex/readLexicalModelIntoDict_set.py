# encoding: utf-8

def main():
	import sys
	import os
	from operator import itemgetter

	if len(sys.argv) != 2:
		print 'Usage: python', sys.argv[0], 'input-lexical'
		exit()

	lex_name = sys.argv[1]
	
	dictLex = readLex(lex_name,'e2f')
	
	user_input = ''
	while True:
		user_input = raw_input('>>> Input phrase (or "exit" to quit): ')
		try: 
			if tryToExit(user_input): break
			candidate_list = dictLex[user_input]
			#maximum_prob_item = selectMaxProb(candidate_list)
			print '>>> The word "%s" in the dictionary contain(s) the following options:' % user_input
			print candidate_list
			# update 2d array to set
			#candidate_list = sorted(candidate_list, key=itemgetter(1), reverse=True)
			#for ele in candidate_list:
				#print ele[0], '=', ele[1] 
			#print '>>> The word "%s" in the dictionary contain(s) the following options:\n' % user_input, maximum_prob_item
		except KeyError:
			if tryToExit(user_input): break

def selectMaxProb(candidates):
	current = ['', '0']
	for item in candidates:
		if float(item[1]) > float(current[1]):
			current[0], current[1] = item[0], item[1]

	return current

def tryToExit(user_input):
	if user_input == 'exit':
		tmp_input = raw_input('>>> Are you sure to exit? (y/n): ')
		if tmp_input in 'Yy':
			print 'Thank you for using this dictionary, goodbye!'
			return True

def readLex_set(lex_file,order):
	fr_lex = open(lex_file, 'r')
	output_dict = {}
	key_set = set()
	import sys
	line_id = 0
	for line in fr_lex:
		line_id += 1
		if line_id % 10000 == 0: 
			sys.stdout.write('lines: %d	keys: %d \r' % (line_id, len(output_dict.keys())))
			sys.stdout.flush()
		try:
			if order == 'e2f':
				sep_lex = line.strip().split(' ',1) # split the first space only
			elif order == 'f2e':
				sep_lex = line.strip().split(' ')
			if order == 'e2f':
				sep_index = sep_lex[0]
			elif order == 'f2e':
				sep_index = sep_lex[1]
			if sep_index not in key_set:
				if order == 'e2f':
					#output_dict[sep_index] = [sep_lex[1].split(' ')] # update 2d array to set
					output_dict[sep_index] = set()
					output_dict[sep_index].add(sep_lex[1].split(' ')[0])
				elif order == 'f2e':
					#output_dict[sep_index] = [[sep_lex[0], sep_lex[2]]] # update 2d array to set
					output_dict[sep_index] = set()
					output_dict[sep_index].add(sep_lex[0])
				key_set.add(sep_index)
			else:
				if order == 'e2f':
					#print [sep_lex[1], sep_lex[2]]
					#output_dict[sep_index].append(sep_lex[1].split(' ')) # update 2d array to set
					output_dict[sep_index].add(sep_lex[1].split(' ')[0])
				elif order =='f2e':
					#output_dict[sep_index].append([sep_lex[0], sep_lex[2]]) # update 2d array to set
					output_dict[sep_index].add(sep_lex[0])
		except KeyError:
			print 'KeyError -%s-' % sep_index, line.strip()

	fr_lex.close()
	return output_dict

if __name__ == '__main__':
	main()
