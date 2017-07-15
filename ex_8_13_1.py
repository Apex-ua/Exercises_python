def acunama(tot):
	del tot[0]
	n = len(tot)-1
	del tot[n]
	
t = ['a', 'b', 'c']
acunama(t)
print t