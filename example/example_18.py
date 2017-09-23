#
#
#
Tn=0
Sn=[]
num=int(input('please input the base number:'))
times=int(input('please input the number of times:'))
for i in range(times):
	Tn = Tn + num
	num=num*10
	Sn.append(Tn)
print(Sn)
