def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		
def pre_corpus(zh_f,lan):
	print '########Reading Wiki_Doc' + ' From file "' + zh_f + '"###########'
	
	
	#len_p = number_file(file)
	front = zh_f[:-3]
	last = zh_f[-3:]
	#out_n_zh = front +'.clean' + last
	out_n_zh = zh_f +'.clean'
	
	rm_list = []
	
	if lan == 'en':
		default_num = 80
	elif lan == 'zh':
		default_num = 63
		#1.18:1(en,zh)
	
		import uniout
		#line_num,original_line
# with is like your try .. finally block in this case
	data = []
	with open(zh_f, 'r') as file:
		# read a list of lines into data
		for line in file:
			data.append(line)

	ok_lines = []
	for line in data:
		splited = line.split(' ')
		if len(splited) < default_num:
			ok_lines.append(line)
	#print data
# and write everything back
	with open(out_n_zh, 'w') as file:
		file.writelines( ok_lines )
	
		
	print '########End###########'
	return 1

def main():
	import sys
	if len(sys.argv) != 3:
		print 'Usage: python', sys.argv[0], 'input-file-zh' , '[en,zh]'
		exit()
	zh_f = sys.argv[1]
	lan = sys.argv[2]
	pre_corpus(zh_f,lan)

if __name__ == "__main__":
	main()