def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		
def pre_corpus(zh_f,tmp_f):
	print '########Reading Wiki_Doc' + ' From file "' + zh_f + '"###########'
	
	
	#len_p = number_file(file)
	
	out_n_zh = zh_f+'.re'
	tmp = []
	
	with open(tmp_f) as f:
		for re_line in f:
			tmp.append(re_line.split(':', 1 ))
		
		#line_num,original_line
# with is like your try .. finally block in this case
	with open(zh_f, 'r') as file:
		# read a list of lines into data
		data = file.readlines()

	print len(data)
	'''
	for x in range(0,len(tmp),2):
		line_num = int(tmp[x][0]) - 1
		#print line_num
		line_content = tmp[x][1]
		data.insert(line_num, line_content) 
		#data[line_num] = line_content
	'''
	for y in range(0,len(data)):
		#print data[y]
		if data[y][:7] == '$$$$$$$' or data[y][:7] == '@@@@@@@':
			#print 'ok %s ' % data[y]
			
			#print data[0][:7]
			#print data[1][:5]
			#if y == 0:
			#	print data[y]
			#	print data[y+1]
			line_content = tmp.pop(0)[1]
			data[y] = line_content
			
# and write everything back
	with open(out_n_zh, 'w') as file:
		file.writelines( data )
	
		
	print '########End###########'
	return 1

def main():
	import sys
	if len(sys.argv) != 3:
		print 'Usage: python', sys.argv[0], 'input-file-zh' , 'file-tmp'
		exit()
	zh_f = sys.argv[1]
	tmp_f = sys.argv[2]
	pre_corpus(zh_f,tmp_f)

if __name__ == "__main__":
	main()