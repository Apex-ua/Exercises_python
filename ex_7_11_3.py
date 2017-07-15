sum = 0
count = 0
average = 0

filename = raw_input('Enter a file name: ')
if filename == 'na na boo boo':
	print "NA NA BOO BOO TO YOU - You have been punk'd!"
	exit()
try:
	temp = open(filename)
except: 
	print 'File dont exist.' 
	exit()

for line in temp:
	if line.startswith('X-DSPAM-Confidence:') :
		aftcln = line.find(':')
		lengthh = len(line)
		code = line[aftcln + 2:lengthh]
		code = float(code)
		sum += code
		count += 1
if sum != 0 and count != 0:
	average = sum / count
	print 'Average spam confidence: %s' % (average)		