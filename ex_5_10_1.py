total=0
count=0
average=0
while True:
	line = raw_input('> ')
	if line == 'done':
		break
	try:
		line = float(line)
		total += line
		count += 1
	except:
		print 'Please enter a number'

if total != 0 and count != 0:
	average = total / count
print 'Total: %s, entered %s, average is %s' % (total,count,average)		