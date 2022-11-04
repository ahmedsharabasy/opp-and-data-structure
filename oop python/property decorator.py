class member:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        return f"hello {self.name}"
    

    @property
    def age_in_days(self):
        return self.age*365


one=member("ahmed",20)
print(one.say_hello())
#print(one.age_in_days())
print(one.age_in_days)  #بتساوى الى فوق لما نحط قبل الفانكشن @property