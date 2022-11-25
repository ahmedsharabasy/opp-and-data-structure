def addition(n1,n2):
    if type(n1) !=int or type(n2)!=int:
        print("only integerrs allowed")
    else:            
        print(n1+n2)

addition(100,200)  

##############################################################
def full_name(first,middle,last):
    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("ahmed","khaled","Elsharabasy")


##############################################################
#packing ,unpacking argument           (*argument)

print(1,2,3,4,5)
mylist=[1,2,3,4,5]
print(mylist)
print(*mylist)


#def say-Hello(*peoples)         اما ابق مش عارف عدد الارجيومنتس  دى مكان الخطوتين الى تحت
def say_Hello(n1,n2,n3,n4):
    peoples=[n1,n2,n3,n4]   

    for name in peoples:
        print(f"hello {name}")

say_Hello("ahmed","mohamed","sayed","ali")

#######################################################3

def show_details(skill1,skill2,skill3):
    print("hello Ahmed your skills is:")

    print(f"{skill1}")
    print(f"{skill2}")
    print(f"{skill3}")

show_details("python","c++","c#") 

def show_details(name,*skills):
    print(f"hello {name} your skills is:")

    for skill in skills:
        print(skill)

show_details("mohamed","python","c++","c#","oop","php") 
########################################################3
#keyword argument
#**  =>dictionary
myskills={
    'HTML':"80%",'oop':"70%",'java':"0%"
}

def show_skills(**skills):
    print(type(skills))

    for skill,value in skills.items():
        print(f"{skill}  =>  {value}")


#show_skills(oop="80%",c_sharp="70%")
print(myskills)
show_skills(**myskills)                         #**بتفك عناصر الدكشنرى تحت بعض

####################################################################3
#                 recursion

#x="wwwoooooorld"
#print(x[1:])
            #عندى كلمة و عايز اطبعها من غير ما يكون فيها احرف متتكرة
def cleanWord(word):
    if len(word)==1:
        return word

    if word[0]==word[1]:
        return cleanWord( word[1:])
    return word[0]+cleanWord(word[1:])


print(cleanWord('wwwwooorrlddd'))        















