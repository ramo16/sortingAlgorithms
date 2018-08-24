#binary search

data=[1,2,3,4,5,6,7,8,9,21,33,45,67,86,99]

"""
def binary_search(data,target,low,high):
	if low> high:
		return False
	else:
		mid=((low+high)//2)
		if target==mid:
			return True
		elif target<data[mid]:
			return binary_search(data,target,low,mid-1)
		else:
			return binary_search(data,target,mid+1,high)
		

print binary_search(data,10,0,8)

"""


def binary_search(data,target,high,low):
	if low>high:
		return False
	else:
		mid=((low+high)//2)
		if target== data[mid]:
			return True
		elif target>data[mid]:
			return binary_search(data,target,high,mid+1)
		else:
			return binary_search(data,target,mid-1,low)
#	else:
#		return False
print binary_search(data,67,14,0)
print binary_search(data,3,14,0)
print binary_search(data,6,14,0)
print binary_search(data,7,14,0)
print binary_search(data,190,14,0)

