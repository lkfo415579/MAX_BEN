#3/31/2015, this tool is for 
def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		
def pre_corpus(zh_f,tmp_f):
	print '########Reading Wiki_Doc' + ' From file "' + zh_f + '"###########'
	
	
	#len_p = number_file(file)
	
	out_n_zh = zh_f+'.delete'
	tmp = []
	
	with open(tmp_f) as f:
		for re_line in f:
			tmp.append(re_line.split(':', 1))
# with is like your try .. finally block in this case
	with open(zh_f, 'r') as file:
		# read a list of lines into data
		data = file.readlines()

	print len(data)

	for y in tmp:
		#y = [100,sentence]
		#line should be - 1 , because it is an array
		if y[1][:6] != '</doc>':
			data[int(y[0])-1] = "$$$$$$$\n"
		else:
			data[int(y[0])-1] = "@@@@@@@\n"
			
# and write everything back
	with open(out_n_zh, 'w') as file:
		file.writelines( data )
	
		
	print '########End###########'
	return 1

def main():
	import sys
	if len(sys.argv) != 3:
		print 'Usage: python', sys.argv[0], 'input-file' , 'file-tmp'
		exit()
	zh_f = sys.argv[1]
	tmp_f = sys.argv[2]
	pre_corpus(zh_f,tmp_f)

if __name__ == "__main__":
	main()