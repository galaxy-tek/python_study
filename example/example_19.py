#
#
#
from sys import stdout
for j in range(2,1001):
	k=[]
	n=-1
	s=j
	for i in range(1,(int(j/2)+1)):
		if j % i == 0 :
			n = n+1
			s = s-i
			k.append(i)
	if s == 0 :
		print(j)
		for i in range(n):
			stdout.write(str(k[i]))
			stdout.write("*")
		print(k[n])

