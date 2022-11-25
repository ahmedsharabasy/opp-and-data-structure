#reduce()     شبه الماب والفلتر فى الشكل لكن المضمون بتمسك عنصرين تتطبق عليهم الفانكشن ثم تمسك الناتج وتطبق عليه الفانكشن مع العنصر الى بعده وهكذا
from functools import reduce
def sumnum(n1,n2):
    return n1+n2

x=[1,2,3,4,5,6]
result=reduce(sumnum,x)    
print(result)        #(((((1+2)+3)+4)+5)+6)