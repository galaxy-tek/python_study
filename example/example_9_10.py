##
##
import time
for i in range(1,10):
	time.sleep(1)
#	print(time.localtime(time.time()))
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	

