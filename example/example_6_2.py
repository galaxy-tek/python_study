##
##
def recursive(i):
	sum=0
	if i==0:
		return 1
	else:
		sum=i*recursive(i-1)
	return sum



def hanoi(n,A,B,C):
	if n>0:
#		print('%d: %s-->%s'%(n,A,C))
#	else:
		hanoi(n-1,A,C,B)
		print('%d: %s-->%s'%(n,A,C))
		hanoi(n-1,B,A,C)

hanoi(4,'A','B','C')
