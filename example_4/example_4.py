##
##
year=int(input('please input Year:'))
month=int(input('please input Month:'))
if month>12:
	print ('Month value is out of range!')
day=int(input('please input Day:'))
if day>31:
	print('Day value is out of range!')

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#month_days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
leap=0
if ((year%400==0) or ((year%100!=0) and (year%4==0))):
	leap = 1
sum=0
for i in range(0,month):
	sum+=month_days[i]
sum+=day
sum+=leap
print(sum)