#encoding: utf-8
from optparse import OptionParser, SUPPRESS_HELP , OptionGroup
def main():
	usage = "Date:6/9/2017\n"+"Usage: %prog [-h] [-r|-t|-l] [[sub_options] arg]"+"\n"
	parser = OptionParser(usage,add_help_option=False)
	parser.add_option("-h", "--help",	action="help",	help="Display Help Menu Again.")
	
	group = OptionGroup(parser, "Prepare-Training-Save Options")
	group.add_option("-r","--run",	dest="train",			default=False,					help="Start Prepare-Training-Save.",	action="store_true")
	group.add_option("--rs",		dest="sourcefile_r",	default="zh-en/train/ted.zh",	help="Sourcefile name.[default: %default]")
	group.add_option("--rt",		dest="targetfile_r",	default="zh-en/train/ted.en",	help="Targetfile name.[default: %default]")
	group.add_option("--rlm",		dest="lexical",			default="zh-en/lex/lex.e2f",			help="Lexical_Model name.[default: %default]")
	group.add_option("--rm",		dest="outputmodel",		default="zh-en/model/model.p",		help="Output maximum entropy model name.[default: %default]")
	group.add_option("--rf",		dest="outputfeature",	default="no",					help="Output featuresets file name.[default: %default]")
	group.add_option("--re",		dest="testset",			default=0.02,	type="float",	help="DAMN The percentage of testset size.[default: %default]")
	group.add_option("--rc",		dest="cores",			default=8,		type="int",		help="The amount of cores.[default: %default]")
	#group.add_option("--ro",		dest="order",			default="e2f",					help="The order of lexical model.[default: %default]")
	group.add_option("--rTFPN",		dest="TFPN",			default=1000,	type="int",		help="The amount of testset for TFPN.[default: %default]")
	parser.add_option_group(group)
	

	group2 = OptionGroup(parser, "Load-Test-Find Options")
	group2.add_option("-t","--test",	dest="test",			default=False,					help="Start Load-Test-Find.",	action="store_true")
	group2.add_option("--ts",			dest="sourcefile_t",	default="zh-en/test/test.zh",	help="Sourcefile name.[default: %default]")
	group2.add_option("--tt",			dest="targetfile_t",	default="zh-en/test/test.en",	help="Targetfile name.[default: %default]")
	group2.add_option("--tlm",			dest="lexical",			default="zh-en/lex/lex.e2f",			help="Lexical_Model name.[default: %default]")
	#group2.add_option("--tor",			dest="order",			default="e2f",					help="The order of lexical model.[default: %default]")
	group2.add_option("--tm",			dest="model",			default="zh-en/model/model.p",		help="maximum entropy model name.[default: %default]")
	group2.add_option("--tw",			dest="wrong_rate_t",	default=0.95,	type="float",	help="WRONG RATE greater than.[default: %default]")
	group2.add_option("--to",			dest="ok_rate_t",		default=0.95,	type="float",	help="OK RATE greater than.[default: %default]")
	group2.add_option("--tc",			dest="cores",			default=8,		type="int",		help="The amount of cores.[default: %default]")
	group2.add_option("--tf",			dest="outputfile",		default="zh-en/output",		help="Outputfile(ok,mid,wrong) ,total 3 files.[default: %default]")
	group2.add_option("--te",			dest="testset",			default=0.001,	type="float",	help="The percentage of testset size.[default: %default]")
	group2.add_option("--ts_text",		dest="sourcefile_t_origin",	default="",					help="unprocess of sourcefile name.[default: %default]")
	group2.add_option("--tt_text",		dest="targetfile_t_origin",	default="",					help="unprocess of targetfile name.[default: %default]")
	parser.add_option_group(group2)
	
	group3 = OptionGroup(parser, "Lexfilter Options")
	group3.add_option("-l", "--lexfilter",	dest="lex",	action="store_true",		help="Start filtering lexical model.",	default=False)
	group3.add_option("--ll",	dest="ori_lex",		default="zh-en/lex",					help="Original Lexical Model name.[default: %default]")
	group3.add_option("--lo",	dest="order",		default="e2f",							help="The order of lexical model.[default: %default]")
	group3.add_option("--lh",	dest="threshold",	default=0.02,	type="float",			help="Filter Word's Pro is less than.[default: %default]")
	group3.add_option("--lt",	dest="top",			default=False,	action="store_true",	help="Enable Filter Top 10 Words.[default: %default]")
	group3.add_option("--ls",	dest="symbol",		default=True,	action="store_false",	help="Disable filter symbol.[default: %default]")
	group3.add_option("--lc",	dest="chinese",		default=True,	action="store_false",	help="Disable filter chinese.[default: %default]")
	parser.add_option_group(group3)

	group4 = OptionGroup(parser, "Load-Test-Match Options")
	group4.add_option("-m","--match",	dest="match",			default=False,	action="store_true",	help="Start Load-Test-Match. ")
	group4.add_option("--ms",			dest="sourcefile_m",	default="zh-en/200.test.zh",			help="Sourcefile name.[default: %default]")
	group4.add_option("--mt",			dest="targetfile_m",	default="zh-en/200.test.en",			help="Targetfile name.[default: %default]")
	group4.add_option("--mlm",			dest="lexical",			default="zh-en/zh2e_f",					help="Lexical_Model name.[default: %default]")
	#group2.add_option("--tor",			dest="order",			default="e2f",							help="The order of lexical model.[default: %default]")	
	group4.add_option("--mm",			dest="model",			default="object/model.p",				help="maximum entropy model name.[default: %default]")
	group4.add_option("--mh",			dest="ok_rate",			default=0.95,	type="float",			help="OK RATE greater than.[default: %default]")
	group4.add_option("--mw",			dest="win_size",		default=0.06,	type="float",			help="Windows size = % of corpus.[default: %default]")
	group4.add_option("--mc",			dest="cores",			default=12,		type="int",				help="The amount of cores.[default: %default]")
	group4.add_option("--mo",			dest="outputfile_m",	default="match/1000.test.match",		help="Outputfile name.[default: %default]")
	group4.add_option("--m_sort",		dest="m_sort",			default=True,	action="store_false",	help="Disable sort the original file.[default: %default]")
	group4.add_option("--ms_text",		dest="sourcefile_t_origin",	default="",							help="unprocess of sourcefile name.[default: %default]")
	group4.add_option("--mt_text",		dest="targetfile_t_origin",	default="",							help="unprocess of targetfile name.[default: %default]")
	parser.add_option_group(group4)
	
	(options, args) = parser.parse_args()
	
	'''
	print 'args', args
	print 'options', options
	'''
	main_option_count = int(options.train) + int(options.test) + int(options.lex) + int(options.match)
	
	if main_option_count > 1:
		parser.error("you only can pick one of the main actions.")
	elif main_option_count == 0:
		parser.error("you have atleast pick one of the main actions.")
	'''
	if len(args) != 1:
		parser.error("incorrect number of arguments")
	if options.verbose:
		print "reading %s..." % options.filename
	'''
	
	if options.train:
		#this guy run train option.
		max_args = {
			'zh_dir':options.sourcefile_r,
			'en_dir':options.targetfile_r,
			'cores':options.cores,
			'lex_table':options.lexical,
			'len_test_sets':options.testset}
		m_c.auto(max_args)
		##TFPN
		m_c.TFPN(options.TFPN,0)
		##after training model
		save_args = {
			'class_output_file':options.outputmodel,
			'f_sets_output_file':options.outputfeature,
			'id_f':0}
		m_c.save(save_args)
	elif options.test:
		pre_args =  {
			'class_file':options.model,
			'f_sets_file':'no'}
		m_c.load(pre_args)
		find_args = {
			'zh_dir':options.sourcefile_t,
			'en_dir':options.targetfile_t,
			'ok_rate':options.ok_rate_t,
			'wrong_rate':options.wrong_rate_t,
			'cores':options.cores,
			'output':options.outputfile,
			'lex_table':options.lexical,
			'len_test_sets':options.testset,
			'targetfile_t_origin':options.targetfile_t_origin,
			'sourcefile_t_origin':options.sourcefile_t_origin}
		#omg i will change it later
		m_c.find_wrong(find_args)
	elif options.match:
		pre_args =  {
			'class_file':options.model,
			'f_sets_file':'no'}
		m_c.load(pre_args)
		match_args = {
			'zh_dir':options.sourcefile_m,
			'en_dir':options.targetfile_m,
			'ok_rate':options.ok_rate,
			'cores':options.cores,
			'output':options.outputfile_m,
			'lex_table':options.lexical,
			'win_size':options.win_size,
			'sort':options.m_sort,
			'targetfile_t_origin':options.targetfile_t_origin,
			'sourcefile_t_origin':options.sourcefile_t_origin}
		#omg i will change it later
		m_c.find_match(match_args)
	elif options.lex:
		lex_args =  {
			'filename':options.ori_lex,
			'less_than':options.threshold,
			'order':options.order,
			'top':options.top,
			'symbol':options.symbol,
			'chinese':options.chinese}
		m_c.l(lex_args)

import wrapper.m_c as m_c
if __name__ == "__main__":
	import sys
	try: 
		if sys.argv[1] == None:
			no_arg = True
	except IndexError:
		sys.argv.append('-h')
	
	main()
