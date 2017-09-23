##
##
##
count=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (i!=k) and (j!=k):
				print(i, end='')
				print(j, end='')
				print(k)
#				result=100*i+10*j+k
				count=count+1
#				print("%d:%d"%(count,result))
print ("count:%d"%(count))

				


