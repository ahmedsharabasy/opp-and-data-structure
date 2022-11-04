class member:
    def __init__(self,fname,mname,lname,gender):
        self.fname=fname         #attribute
        self.mname=mname
        self.lname=lname
        self.gender=gender

    def fullname(self):
        return f"{self.fname} {self.mname} {self.lname}"     

    def hello(self):
        if self.gender=="male":
            return f"hello mr {self.fname}"     
        elif self.gender=="female":
            return f"hello miss {self.fname}"
        else:
            return f"hello {self.fname}"        


member1=member("mohamed","ali","hessin","male")
member2=member("mona","gomma","ramadan","female")

print(member1.mname)
print(member2.mname)
print(member1.fname,member1.mname,member1.lname)
print(member1.fullname())
print(member2.hello())
print(member1.hello()7hhnnn 

