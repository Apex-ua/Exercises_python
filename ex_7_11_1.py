while True:
	filename = raw_input('Enter a file name: ')
	if filename.lower() == 'exit':
		break
	try:
		temp = open(filename)
		for line in temp:
			print line.upper()
	except: 
		print 'File dont exist. Try again or enter "exit"' 
