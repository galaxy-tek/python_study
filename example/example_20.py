#
#
#
height = [] 
tour = []
hei = 100.0
tim = 10
for i in range(1,tim+1):
	tour.append(hei)
	hei = hei/2
	height.append(hei)
print('Total height: %f'%(sum(tour)))
print('height of tenth bounce:%f'%(height[-1]))