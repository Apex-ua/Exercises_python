promt = 'Enter temperature, C: '
input = raw_input(promt)
input = int(input)
temp_f = (input * 1.8)/1.8
temp_f=str(temp_f)
print 'Temperarure in Fahrenheit: ' + temp_f