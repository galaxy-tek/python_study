##
##
num_p=0
num_c=1
num_n=1
for i in range(0,11):
	num_n=num_p+num_c
	print(num_p)
	num_p=num_c
	num_c=num_n

