def computegrade(Score):
	if Score > 0.9 and Score < 1.0:		
		return 'A'
	elif Score > 0.8 and Score < 0.9:		
		return 'B'
	elif Score > 0.7 and Score < 0.8:		
		return 'C'
	elif Score > 0.6 and Score < 0.7:		
		return 'D'
	elif Score <= 0.6:		
		return 'F'
	elif Score > 1.0:		
		return 'Bad score'	

	
	
input=raw_input('Enter Score: ')

try:
	input=float(input)
	Fir=computegrade(input)
	print Fir
except:
	print 'Bad score'