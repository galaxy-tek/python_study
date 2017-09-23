##
##
import math
count = 0
leap = 1 
for m in range(101,201):
	k=int(math.sqrt(m))
	for i in range(2,k+2):
		if m%i == 0 :
			leap = 0
			break
	if leap == 1 :
		count += 1
		print(m)
		if count % 10 == 0:
			print ('')
	leap = 1 
print(' ')
print('The total is %d'%count)
			



