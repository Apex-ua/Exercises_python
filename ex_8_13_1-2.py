def middle(tot):
	first = tot.pop(0)
	n = len(tot)-1
	last = tot.pop(n)
	un = []
	un = first + last
	return un
	
	
t = ['a', 'b', 'c']

lists = []
lists = middle(t)
print lists