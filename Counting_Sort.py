def countingsort( aList, k ):
	counter = [0] * ( k + 1 )
	for i in aList:
		counter[i] += 1

	print counter

	ndx = 0;
	for i in range( len( counter ) ):
		while 0 < counter[i]:
			aList[ndx] = i
#			print i
			ndx += 1
			counter[i] -= 1
			print counter



alist=[1,1,9,3,5,1,8]
countingsort(alist,max(alist))
print alist
