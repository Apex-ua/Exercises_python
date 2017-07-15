def Calcul(Hours,Rate):
	if Hours > 40:
		ExtraHours=Hours-40
		sum=(40*Rate)+(ExtraHours*15)
	else:
		sum=Hours*Rate
	return sum

	
input_h = raw_input('Enter hours: ')
input_h=int(input_h)
input_r = raw_input('Enter rate: ')
input_r=int(input_r)
Pay=Calcul(input_h,input_r)
Pay=str(Pay)
print 'Pay: ' + Pay 
