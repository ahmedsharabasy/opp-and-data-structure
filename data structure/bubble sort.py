def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

array=[8,69,47,25,14,35,21,2,4]
bubblesort(array)
print('bubble sort is:')
print(array,end=' ')
