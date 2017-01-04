#This tool for to eliminate duplicated sentences 
import uniout
import sys
def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		

		
		
		
def Super_filter(data):
	index = 0
	super_checker = 0

	#
	first = True
	for line in data:
		if line[:2] == "OK":
			#first header of doc
			if first:
				#wish_list
				try:
					wish_list.clear()
				except UnboundLocalError:
					wish_list = dict()
				first = False
			##############
			#header of each matched!format data!
			ok_rate = float(data[index][5:-2])
			wrong_rate = 100 - ok_rate
			zh = data[index+4][5:-1]
			en = data[index+5][5:-1]
			#append into wish_list,zh_sentence: [ok_rate,index(header)]
			try:
				wish_list[zh].append([ok_rate,index])
			except:
				wish_list.update({zh: [[ok_rate,index]]})
				
		if line[:6] == "Amount":
			first = True
			#end of each doc
			if wish_list:
				try:
					#import pdb
					#pdb.set_trace()
					#print wish_list
					for match in wish_list:
						if len(wish_list[match]) > 1:
							#print wish_list[match]
							highest_ok_list = max(wish_list[match], key=(lambda k: k[0]))
							#print 'h_index %s' % str(highest_ok_list)
							wish_list[match].remove(highest_ok_list)
							#eliminate other low ok rate sentences
							for info in wish_list[match]:
								#convert them into  ""
								data[info[1]] = ""#OK
								data[info[1]+1] = ""#WRONG
								data[info[1]+2] = ""#line_zh
								data[info[1]+3] = ""#line_en
								data[info[1]+4] = ""#zh
								data[info[1]+5] = ""#en
								data[info[1]+6] = ""#----
								
				except:
					pass
					
		
		#
		index += 1 
		sys.stdout.write('Index: %d\r' % index)
		sys.stdout.flush()
		
	return data
		
def pre_match(match_f):
	print '########Reading match_Doc' + ' From file "' + match_f + '"###########'
	
	front = match_f[:-6]
	out_n = front +'.nosame.match'
	
	data = []
	with open(match_f, 'r') as file:
		# read a list of lines into data
		for line in file:
			data.append(line)
		

	#argv to saved coprus[en,zh]
	oklines = Super_filter(data)
	
	
	# and write zh
	with open(out_n, 'w') as file:
		file.writelines( oklines )
	
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