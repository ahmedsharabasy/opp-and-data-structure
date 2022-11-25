#الفلتر زى الماب فى الكتابة ولكن فيه شوية فروق فى المضمون
#الفلتر بيشيك على شرط يشوفه اما ترو يطبع او فولس ميطبعش

def checkname(name):
    return name.startswith("o")

mytext=["ahmed","omar","ali","osman","osama"]
myreturndata=filter(checkname,mytext)
for person in myreturndata:
    print(person)
#######################################
print('*'*50)
#######################################
#same code with lambda
# def checkname(name):
#     return name.startswith("o")

mytext=["ahmed","omar","khaled","ali","osman","osama"]
myreturndata=filter( lambda person_name: person_name.startswith("a"),mytext)
for person in myreturndata:
    print(person)    
