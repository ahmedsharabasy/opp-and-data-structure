#
# class member:
#     def __init__(self,name):
#         self.name=name

# one=member("Ahmed") 
# print(one.name) 

# one.name="osama"
# print(one.name)

# class member:
#     def __init__(self,name):
#         self._name=name          #اندراسكور قبل الفاريبال يبق الفاريبال protected
#                                  #البروتكتد شبه البابلك بيق مختفى فقط عند الاستدعاء لكن لو كتبته يتكتب عادى

# one=member("Ahmed") 
# print(one._name)    


class member:
    def __init__(self,name):
        self.__name=name          #اتنين اندر اسكور يبق private
                                  #لايمكن استخدمه برا الكلاس
    def hello(self):
        print(f"hello {self.__name}")

one=member("Ahmed") 
one.hello()
#print(one.__name)                 #Error عشان بره الكلاس    

print(one._member__name)
