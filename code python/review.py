# for i in range(0,50):
#     if i/2 !=0:
#         return i


# def linear_search(arr, target):
#     for i in range(0,len(arr)):
#         if arr[i]==target:
#             print(arr[i],'is present in array')

# array=[1,2,3,4,5,6,7,8,9,10]
# linear_search(array,4)

def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return mid-1
        elif arr[mid]<target:
            return mid+1
    else:
        return -1

array={1,2,3,4,5,6,7,8,9,10}
bs=binary_search(array,5)
if bs:
    print(bs,'is found')
else:
    print('item is not found')                            

