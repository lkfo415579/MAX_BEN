import sys
import os
from readLexicalModelIntoDict import readLex
from reorderRuleTable import *
from operator import itemgetter

def main():
	if len(sys.argv) != 7:
		print 'Usage: python', sys.argv[0], 'input-name f e lex alignment output-name'
		exit()

	f = sys.argv[2]
	e = sys.argv[3]
	source_file = sys.argv[1]+'.'+f
	target_file = sys.argv[1]+'.'+e
	lexical_file = sys.argv[4]
	align_file = sys.argv[5]
	output_file = sys.argv[6]
	
	fr_source = open(source_file, 'r')
	fr_target = open(target_file, 'r')
	fr_align = open(align_file, 'r')
	fw_source = open(output_file, 'w')
	
	# read lexical model into dictionary
	my_dict = {}
	my_dict = readLex(lexical_file)
	
	index = 0
	while True:
		line_source = fr_source.readline().strip()
		line_target = fr_target.readline().strip()
		line_align = fr_align.readline().strip()
	
		if not line_source or not line_align:
			break
	
		# separate space
		sep_source = line_source.split(' ')
		sep_target = line_target.split(' ')
		sep_align = line_align.split(' ')

# processing the alignment to one-to-one	
		# extract the source alignment index from the alignment file
		# since the alignment is sorted in the target side
		ol = set()
		tmp_dict = {} # 0 = [0,1,4,5]
		for ele in sep_align:
			ele_split = ele.split('-')
			if ele_split[0] not in ol:
				ol.add(int(ele_split[0]))
				tmp_dict[ele_split[0]] = [int(ele_split[1])]
			else:
				tmp_dict[ele_split[0]].append(int(ele_split[1]))
		
		# dictionary to 2d array
		align_array = []
		for key, value in tmp_dict.iteritems():	
			align_array.append([key, value])
		one2one_alignment = selectAlign(line_source, line_target, align_array, my_dict)
                #reformAlignStr = reformAlign(seplll[0], skipResultStr, model)

		tmp_list = sorted(one2one_alignment, key=itemgetter(1))
		ol = map(lambda x: x[0], tmp_list)

		# insert the missing alignment into list
		max_index = len(sep_source)
		for ele in range(0, max_index):
			if str(ele) not in ol:
				ol.insert(ol.index(str(ele - 1)) + 1 if ele > 0 else 0, str(ele))
		
		# debug print
		index += 1
	#	print ' '.join(ol)
	#	if index > 48620:
	#		print index, max_index, ol	
	#		print line_source
	
		# preorder the source language
		output = []
		for ele in ol:
			output.append(sep_source[int(ele)])
	
		fw_source.write(' '.join(output) + '\n')
	
	fr_source.close()
	fr_target.close()
	fr_align.close()
	fw_source.close()

if __name__ == '__main__':
	main()
