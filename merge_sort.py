#suhail merge_sort


def merge_sort(alist):
    print alist
    if len(alist)>1:
        mid= len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=0
        j=0
        k=0

        while i<len(lefthalf) and j< len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i< len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
                        


alist=[0,9,8,7,6,5,4,3,2,1,3,5,7]
merge_sort(alist)
print alist



