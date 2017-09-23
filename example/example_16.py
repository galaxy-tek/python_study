#
#
#
import string
s= input('please input a string:')
letters=0
spaces=0
digit=0
others=0
for c in s:
	if c.isalpha():
		letters+=1
	elif c.isspace():
		spaces+=1
	elif c.isdigit():
		digit+=1
	else:
		others+=1
print('letters=%d, spaces=%d, digit=%d, others=%d'%(letters,spaces,digit,others))


