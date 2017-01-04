def RE_search(file_name):
	import re, mmap
	phrase = '<doc.*?>(?:[^\n]*(\n+))*?<\/doc>'
	with open(file_name, 'r+') as f:
		data = mmap.mmap(f.fileno(), 0)
		mo = re.search(phrase, data)
		if mo:
			content = mo.group()
			print file_name
	
	try:
		return content
	except:
		return False
	#when it gets first one , it will be stooped.
	
def number_file(dir):
	with open(dir) as f:
		return sum(1 for _ in f)
		
def pre_corpus(zh_f,en_f):
	print '########Reading Wiki_Doc' + ' From file "' + zh_f+' '+en_f + '"###########'
	
	zh_pages = RE_search(zh_f)

	print zh_pages
	#len_p = number_file(file)
	
	out_n_zh = zh_f[:-3]+'.tok.zh'
	out_n_en = en_f[:-3]+'.tok.en'
	
	output_zh = open(out_n_zh, "wa")
	output_en = open(out_n_en, "wa")
	
	
	
		
	print '########End###########'
	return 1

def main():
	import sys
	if len(sys.argv) != 3:
		print 'Usage: python', sys.argv[0], 'input-file-zh' , 'input-file-en'
		exit()
	zh_f = sys.argv[1]
	en_f = sys.argv[2]
	
	pre_corpus(zh_f,en_f)

if __name__ == "__main__":
	main()