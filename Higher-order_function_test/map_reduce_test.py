##
##
def f(x) :
	return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

##reduce
from functools import reduce
def add(x,y):
	return x+y

sum = reduce(add,[1,2,3,4,5,6,7,8,9])
print (sum)
