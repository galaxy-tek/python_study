##
##
def fib1(n):
	if n==1 or n==2:
		return 1
	return fib1(n-1)+fib1(n-2)
print (fib1(10))

def fib2(n):
	if n==1:
		return [1]
	if n==2:
		return [2]
	fibs=[1,1]
	for i in range(2,n):
		fibs.append(fibs[-1]+fibs[-2])
	return fibs
print (fib2(10))


