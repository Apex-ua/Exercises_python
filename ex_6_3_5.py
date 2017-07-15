str = 'X-DSPAM-Confidence: 0.8475'
aftcln = str.find(':')
endof = len(str)
code = str[aftcln + 2:endof]
code = float(code)
print type(code)
