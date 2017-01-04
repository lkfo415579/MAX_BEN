#encoding=utf-8

import re
import sys

def check_digit_date(s):
	ans = False

	rea = []

	rea.append('([0-2]?\d|3[01])(-|\/|\.)([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)(\d{2}|\d{4})|([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)([0-2]?\d|3[01])(-|\/|\.)(\d{2}|\d{4})|([0-2]?\d|3[01]|first|third|second|[\w]+th)(th|st|rd|nd)?(\sof)?(\s(January|February|March|April|May|June|July|August|September|October|November|December))((\,)?(\s?in)?(\s(\d{4}|\s\'\d{2})))?|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|second|third|\w+th))(th|st|rd|nd)?\,?(\s?(in|of))?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sof|\,)?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|third|second|\w+th))(th|st|rd|nd)?')
	rea.append('([一二\d][一二三四五六七八九零\d]{3}\s?年\s?[的]?)?[十\d]?[一二三四五六七八九十\d]\s?月\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号)|[一二\d][一二三四五六七八九零\d]{3}\s?年的?\s?[十\d]?[一二三四五六七八九十\d]\s?月(\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号))?|[12]?[09]?\d\d[- /.][0-3]?[0-9][- /.][0-3]?[0-9]')
	rea.append('\d+')
	rea.append('(NULL)')
	#rea.append('[\¼ \。\、\◆\◇\○\◎\●\·\`\^\¨\~\×\≠\≤\=\≥\°\│\─\_\-\,\:\!\?\/\`\-\.\‘\’\(\)\{\}\§\@\¤\$\€\*\\\#\%\+\±\←\→\↑\↓\╱\ˉ\，]')
	#rea.append('[\¨\~\!\@\#\$\%\^\&\*\(\)\-\+\=\[\]\{\}\`\;\:\'\",.<>\/\?\\\|]')
	#rea.append('[(){}§@¤$€*\#%+±←→↑↓╱ˉ，]')
	#rea.append('[`^¨~×≠≤=≥°│─_-,:!?/`-.‘’(){}§@¤$€*\#%+±←→↑↓╱ˉ，]')

	for i in rea:
		reacomp = re.compile(i.decode('utf8'))
		match = reacomp.finditer(s.decode('utf8'))

		for word in match:
			ans = True
			break

		if ans:
			break

	return ans

'''
 * [check_chinese]
 * @param  {[String]} s [english only]
 * @return {[Boolean]}   [True | False]
'''
def check_chinese(s):
	##
	de = s.decode('utf8')
	len_ori = len(de)
	en = de.encode('utf8')
	len_after = len(en)
	return (len_after > len_ori)



def check_symbol(s):
	rea = u"[^a-zA-Z0-9\u4e00-\u9fa5]"
	de = s.decode('utf8')
	
	#print en + 'len' + str(len(en))
	regexboject = re.compile(rea)
	match = regexboject.search(de)
	if match:
		#print("find : %s" % match.group())
		return True

	return False

'''
s = ['天下','下','1234','12天']

for w in s:
	print check_digit_date(w)
'''