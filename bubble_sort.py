def bubble_sort(array):
	for j in range(len(array)-1,0,-1):
		for i in range(j):
			if array[i]>array[i+1]:
				temp=array[i]
				array[i]=array[i+1]
				array[i+1]= temp
				print i

array=[9,8,7,6,5,4,3,2,1,11]
bubble_sort(array)
print array
