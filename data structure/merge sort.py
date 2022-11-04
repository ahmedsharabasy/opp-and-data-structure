def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)   #recursion
        mergesort(r)
        i=j=k=0
        while(i<len(l)and j<len(r)):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1



        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
 
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergesort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)            
