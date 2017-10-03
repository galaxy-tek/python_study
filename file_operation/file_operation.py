##
##read the whole text file with sigle read()
#data.txt
#Line 1 : Data 1
#Line 2 : Data 2
#Line 3 : Data 3
#Line 4 : Data 4
#Line 5 : Data 5


fHandle = open("data.txt", "r")
readStr = fHandle.read()
print(readStr)
fHandle.close()

##
##read the file line by line with for loop
fHandle = open("data.txt", "r")
for readStr in fHandle :
	print(readStr)
fHandle.close()

##
##read the file line by line with while loop
fHandle = open("data.txt", "r")
while 1:
	readStr = fHandle.readline()
	if not readStr :
		break
	print(readStr)
fHandle.close()


##
##write text into a file
fHandle = open("output.txt", "w")
for i in range(1,5) :
	fHandle.write("Line " + str(i) +"\n")
fHandle.close()
