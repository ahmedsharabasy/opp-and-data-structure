def selectionsort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

array=[8,45,78,32,10,9,22,55,44]
selectionsort(array)
print('sorted array is: ')
print(array,end=' ')                