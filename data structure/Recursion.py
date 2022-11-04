def factorial(num):
    if num<=0:
        return        #return فاضية توقف العمليه واى عمليات تحتها
    if num %2 !=0:
        print(num)
    factorial(num -1)    

factorial(100)    


#ده غلط
# def factorial(num):
#     if num>0 and num %2 !=0:
#         print(num)
#     factorial(num -1)    

# factorial(100)    

        