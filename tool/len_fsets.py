def len_fsets(fsets):
	total = 0
	for tmp in fsets:
		total += len(tmp[0])
	print "Total number of featuresets : "+str(total)
