#this is a tool for post_preparing for match file.
#1.length_raito
#2.blankspace
#3.distances between two match lines
#4.determine the OK rate
#final_step.sperate into two files
import uniout
import sys
def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		

def ratio(en,zh):
	#2 times
	ratio = 2
	splited_zh = []
	splited_en = []
	splited_zh = zh.split(' ')
	splited_en = en.split(' ')
	
	#print en
	#print zh
	#print splited_en
	#print splited_zh
	#print 'show_zh %d' % len(splited_zh)
	#print 'show_en %d' % len(splited_en)
	if len(splited_zh) > len(splited_en)*ratio or len(splited_zh)*ratio < len(splited_en) :
		return 1
	else:
		return 0
		
		
def blankspace(en,zh):
	if en == "[blankspace]" or zh == "[blankspace]":
		return 1
	else:
		return 0
		
def distances(line_en,line_zh):
	ratio = 2.5
	if line_zh > line_en*ratio or line_zh*ratio < line_en :
		return 1
	else:
		return 0
		
def check_ok_rate(ok):
	default_ok_rate = 92
	
	if ok < default_ok_rate:
		return 1
	else:
		return 0
		
def Super_filter(data):
	index = 0
	super_checker = 0
	#
	oklines = [[],[]]
	for line in data:
		if line[:2] == "OK":
			#header of each matched!format data!
			ok_rate = float(data[index][5:-2])
			wrong_rate = 100 - ok_rate
			#line_zh = int(data[index+2][11:-1])
			#line_en = int(data[index+3][11:-1])
			zh = data[index+3][5:-1]
			en = data[index+4][5:-1]
			#filter time
			#super_checker += ratio(en,zh)
			#super_checker += blankspace(en,zh)
			#super_checker += distances(line_en,line_zh)
			super_checker += check_ok_rate(ok_rate)
			#append to oklines
			if super_checker == 0:
				oklines[0].append(en + '\n')
				oklines[1].append(zh + '\n')
			else:
				super_checker = 0
		#
		index += 1 
		sys.stdout.write('Index: %d\r' % index)
		sys.stdout.flush()
		
	return oklines
		
def pre_match(match_f):
	print '########Reading match_Doc' + ' From file "' + match_f + '"###########'
	
	front = match_f[:-6]
	out_n_zh = front +'.corpus.zh'
	out_n_en = front +'.corpus.en'
	
	data = []
	with open(match_f, 'r') as file:
		# read a list of lines into data
		for line in file:
			data.append(line)
	
	#zh_lines the final result corpus
	zh_lines = []
	en_lines = []
	
	


	#argv to saved coprus[en,zh]
	oklines = Super_filter(data)
	
	zh_lines = oklines[1]
	en_lines = oklines[0]
	
	# and write zh
	with open(out_n_zh, 'w') as file:
		file.writelines( zh_lines )
	# and write zh
	with open(out_n_en, 'w') as file:
		file.writelines( en_lines )
	
	print '########End###########'
	return 1

def main():
	import sys
	if len(sys.argv) != 2:
		print 'Usage: python', sys.argv[0], 'match-file' 
		exit()
	match_f = sys.argv[1]

	pre_match(match_f)

if __name__ == "__main__":
	main()