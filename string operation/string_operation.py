##
##
aString = "Hello World"
aString_1 = "hello world"
bString = " Python!"
cString = aString + bString
print("cString:",cString)
print("length of cString:",len(cString))
print("aString:",aString)
print("first character of aString",aString[0])
print("aString[4:6]:",aString[4:7])
print("Upper Case:",aString.upper())
print("Lower Case:",aString.lower())
if aString == aString_1 :
	print("aString = aString_1")
else :
	print("Two strings are different.")

if aString.upper() == aString_1.upper() :
	print("Two strings are the same after upper operation.")
else :
	print("Two string are different.")
##
##split a string with a delimiter
##find a substring in a string

dString = "This is an example of string operations in Python"
splitString = dString.split(" ")
print("splitString : ", splitString)
print("The 4th word = ", splitString[3])
print("dString:",dString)
print("find in dString :", dString.find("an"))

##
##converting a number to a string
num1 = 1234
num2 = 5678
str1 = str(num1)
str2 = str(num2)
str_add = str1 + str2
num_add = num1 + num2
print("str_add :", str_add)
print("num_add:", num_add)

##
##writing double quotes in a string
##there are several different ways to writing double quotes in a string
aString = 'He said "Hello World"'
bString = "He said \"Hello World\""
print(aString)
print(bString)

##
##replace a substring in a string
orgStr = "Hello W o r l d ."
replaceHello = orgStr.replace('Hello','Hi')
print(replaceHello)
replacespace = orgStr.replace(' ','')
print(replacespace)

##
##replace a carriage return in a string
orgStr = "\nHello\nWrold"
replaceCR = orgStr.replace("\n"," ")
print("orgstr : ", orgStr)
print("replaceCR :", replaceCR)


##
##covert a hex string into a stream of Hex Numbers(binascii package)
import binascii
hexStr = "AABBCC"
hexNumbers = binascii.a2b_hex(hexStr)
print("hexStr", hexStr)
print("hexNumbers", hexNumbers)
byteArray = bytearray(hexNumbers)
print(byteArray)
print(hexNumbers[0])
print(byteArray[0])

##
##Triming a string
strA = "  Hello World      "
strB = "### Hello Wrold######"
print("strA:",strA)
print("trimmedA=",strA.strip(" "))
print("trimmedB=",strB.strip("#"))








