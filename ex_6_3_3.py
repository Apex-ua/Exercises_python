Ent_wrd = raw_input('Pls, enter word > ')
Ent_lttr = raw_input('And letter > ')


def counter(word,letter):
	count = 0
	for let in word:
		if let == letter:
			count += 1
	return count
	
try:
	if type(Ent_wrd) == str and type(Ent_lttr) == str :
		n = counter(Ent_wrd,Ent_lttr)
		
except:
	print 'Enter a string'
	
	
	
print 'Word %s has %s letter(s) %s' % (Ent_wrd,n,Ent_lttr)
	
