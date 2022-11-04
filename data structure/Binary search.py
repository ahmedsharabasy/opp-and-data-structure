# def Binarysearch(arr,key):
#     left=0
#     right=len(arr)-1
#     index=-1
#     while left<=right and index==-1:
#         mid=(left+right)//2
#         if key==arr[mid]:
#             index=mid
#         else:
#             if key<arr[mid]:
#                 right=mid-1
#             else:
#                 left=mid+1
#     return index

# array=[2,4,6,8,10,22,55,66,77,88,99,101,147,1478]
# index=Binarysearch(array,4)
# if index >=0:
#     print("{} is index {}".format(array[index],index))
# else:
#     print("element not found")    

def Binarysearch(arr,key): 
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if key==arr[mid]:
            return mid
        else:
            if key<arr[mid]:
                right=mid-1
            else:
                left=mid+1
    return mid

array=[2,4,6,8,10,22,55,66,77,88,99,101,147,1478]
index=Binarysearch(array,4)

print(array[index])

if index>=0:
    print("{} is index {}" .format(array[index],index))
else:
    print("element not found")    

 
