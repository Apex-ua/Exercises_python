cl = []
while True:
	line = raw_input('> ')
	if line == 'done':
		break
	try:
		line = float(line)
		cl.append(line)
	except:
		print 'Please enter a number'

MIN = min(cl)
MAX = max(cl)
print "Min is %s, Max is %s" % (MIN,MAX)		