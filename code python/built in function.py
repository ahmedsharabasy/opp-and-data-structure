#1-all()

x=[1,2,3,4,5,False]
if all(x):
    print("all items true")
else:
    print("not all items true")

########################################3
#2-any()

x=[1,2,3,4,5,False]
if any(x):
    print("all items true")
else:
   print(" all items false") 

#  #################################33     
#bin()         #لغه الكمبيوتر

print(bin(10))

#######################################
a=1
b=2
print(id(a))
print(id(b))

#####################################3
#sum(iterable,start)
a=[2,5,5,525,5]
print(sum(a))
print(sum(a,50))

#######################################
#round(number,numof digits)
print(round(151.455,2))
print(round(151.454,2))

###################################
#range(start,end,step)    مبتحسبش اخر رقم يعنى لو end=10 يطبع لحد9
print(list(range(0)))
print(list(range(10)))
print(list(range(0,20,2)))

#######################################3
#print()

print("hello ahmed")
print("hello","ahmed")
print("hello","ahmed",sep=" @ ")


print("ahmed",end=" ")
print("khaled")
print("elsharabasy")


#####################################33
#abs()   بتطلع الرقم السالب موجب

print(abs(-100.44))

#######################################3
#pow(base,exponent,modulsaوده اوبشن)

print(pow(2,4))
print(pow(2,4,10))

###################################
#min()
#max()
print(min(1,5,8,7,9,-2))
print(max("a","k","shfk"))

#slice(start,end,step)
x=[1,2,3,4,5,6,7,8,9]
print(x[slice(2)])
print(x[slice(2,6)])


print("*"*50)
############################################
#enumerate(iterable,start=0)   التعداد بتضيف كونتر للاتريبال الخاص بيك وانت بتعمل عليه لووب
skills=["html","css","js","php"]
skillswithcounter=enumerate(skills,5)
# for skill in skillswithcounter:
#     print(skill)
print(type(skillswithcounter))    
#لو عايز انسقه يبق قبل الخطوه الى فاتت الى جاى
for counter,skill in skillswithcounter:
   print(f"{counter} - {skill}")


#################################################
#reversed()
name="Ahmed"
print(reversed(name))
for i in reversed(name):
    print(i)

