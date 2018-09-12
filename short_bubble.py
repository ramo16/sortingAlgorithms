def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
	       print i
       passnum = passnum-1

alist=[9,8,7,6,5,4,3,2,1,11]
shortBubbleSort(alist)
print(alist)

