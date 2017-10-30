# -*- coding: utf-8 -*-
##
##
import math
h = input("please input your heigh(m): ")
H_int = float(h)
w = input("please input your weight(kg): ")
W_int = float(w)
BMI = W_int/math.pow(H_int,2)
#BMI = W_int/(H_int*H_int)
print("Your BMI is: %.3f"%BMI)
comment = ["too light","normal","too heavy","fat","too fat"]
if (BMI< 18.5) :
	print(comment[0])
elif (BMI < 25) :
	print(comment[1])
elif (BMI < 28) :
	print(comment[2])
elif (BMI < 32) :
	print(comment[3])
else :
	print(comment[4])
