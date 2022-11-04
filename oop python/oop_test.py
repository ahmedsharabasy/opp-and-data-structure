class memmber:
    def __init__(self):
        print("A new member has been added")

memmber()
memmber()
memmber()

print(dir(memmber))    #object

member_one=memmber()     #حطيت الاوبجكت فى فاريبال
member_two=memmber()
member_three=memmber()

print(member_one.__class__)
# ####################################################################

class member:
    def __init__(self,first_name):        #self:create instance from class نستعملها فى كل الفانكشن لاى جوه الكلاس
        self.name='omar'
                 
member_one=member('ahmed')
member_two=member('khaled')
member_three=member('elsharabasy')

print(member_one.name)
print(member_two.name)
print(member_three.name)
print('*'*50)
############################################################
class memberr:
    def __init__(self,first_name):        #  constructor
        self.name=first_name

member_one=memberr('ahmed')
member_two=memberr('khaled')
member_three=memberr('elsharabasy')

print(member_one.name)
print(member_two.name)
print(member_three.name)
print('*'*50)
#############################################################33
class membeerr:

    not_allowed_names=["Hell","shit","Ballot"]               #اتريبيوتس خاصه بالكلاس
    users_num=0

    def __init__(self,first_name,middel_name,last_name,gender):        #self:create insrance from class
        self.fname=first_name
        self.mname=middel_name   #attribute                  #اتريبيوتس خاصه بالانستانس
        self.lname=last_name     #attribute
        self.gender=gender
        membeerr.users_num+=1
    
    def full_name(self):
        if self.fname in membeerr.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:    
            return f"{self.fname} {self.mname} {self.lname}"

    def hello_name(self):
        if self.gender=='male':
            return f"Hello mr {self.fname}"
        elif self.gender=='femele':
            return f"Hello miss {self.fname}" 
        else:
            return f"Hello {self.fname}"

    def get_all_info(self):
        return f"{self.hello_name()}  ,  your full name is {self.full_name()}"

    def delete_user(self):
        membeerr.users_num-=1
        return f"user {self.fname} deleted."        


member_one=membeerr('ahmed','khaled','elsharabasy','male')
member_two=membeerr('mohammed','nasser','saad','mal')
member_three=membeerr('sara','mahmoud','zain','femele')

print(member_one.fname,member_one.mname,member_one.lname)
print(member_two.fname)
print(member_three.fname)

print(member_one.full_name())
print(member_two.full_name())        
print(member_three.full_name())

print(member_one.hello_name())
print(member_three.hello_name())
print(member_two.hello_name())

print (member_one.get_all_info())
print(membeerr.users_num)
print(member_two.delete_user())
print(membeerr.users_num)
           

print('*'*50)
###################################################