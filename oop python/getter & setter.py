class member:
    def __init__(self,name):
        self.__name=name          
                                
    def hello(self):
        print(f"hello {self.__name}")

    def get_name(self):                     #getting
        return self.__name

    def set_name(self,new_name):            #setting
        self.__name=new_name         

one=member("Ahmed") 
one.hello()

print(one._member__name)
print(one.get_name())
one.set_name("Ali")
print(one.get_name())