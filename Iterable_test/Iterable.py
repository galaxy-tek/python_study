##
##
##
from collections import Iterable
d = {'a':1,'b':2,'c':3}
for key in d :
	print(key)

print(isinstance("123",Iterable))
print(isinstance(123,Iterable))

for i, value in enumerate(['A','B','C']):
	print(i, value)

print(list(range(1,11)))

L = [x * x for x in range(1,11)]
print(L)

L = [m+n for m in "ABC" for n in "XYZ"]
print(L)

L = ['Hello', 'World', 18, 'Apple', None]
l=[s.lower() for s in L if isinstance(s,str)]
print(l)

