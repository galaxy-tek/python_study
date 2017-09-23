##
##
for num in range(100,1000):
	a=int(num/100)
	b=int((num-a*100)/10)
	c=num-a*100-b*10
	if num == (a**3+b**3+c**3):
		print(num)
		
	
	


