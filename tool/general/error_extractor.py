def read_corpus(dir):
	print '########Reading Error filex_' + ' From file "' + dir + '"###########'
	file = open(dir, 'r')

	def number_file(dir):
		with open(dir) as f:
			return sum(1 for _ in f)

	#len_p = number_file(file)
	
	output_zh = open(dir+'.zh', "wa")
	output_en = open(dir+'.en', "wa")
	
	corpus = []
	with open(dir , 'r') as file:
		lines = file.read().splitlines()
		for run in range(3,len(lines),6):
			zh_line = lines[run]
			output_zh.write(zh_line[5:]+"\n")
			en_line = lines[run+1]
			output_en.write(en_line[5:]+"\n")
	output_zh.close()
	output_en.close()
		
	print '########End###########'
	return 1

def extract():
	import sys
	if len(sys.argv) != 2:
		print 'Usage: python', sys.argv[0], 'input-file'
		exit()
	input_file = sys.argv[1]
	
	read_corpus(input_file)

if __name__ == "__main__":
	extract()