class membeerr:

    not_allowed_names=["Hell","shit","Ballot"]               #اتريبيوتس خاصه بالكلاس
    users_num=0

    def __init__(self,first_name,middel_name,last_name,gender):        #self:create insrance from class
        self.fname=first_name
        self.mname=middel_name   #attribute                  #اتريبيوتس خاصه بالانستانس
        self.lname=last_name     #attribute
        self.gender=gender
        membeerr.users_num+=1

    @classmethod
    def show_users_count(cls):          #don't require instance
        print(f"we have {cls.users_num} users in our system")
    
    def full_name(self):                               #instance method
        if self.fname in membeerr.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:    
            return f"{self.fname} {self.mname} {self.lname}"

    @staticmethod
    def sayhello():         #static method
        print("hello from static method")


member_one=membeerr('ahmed','khaled','elsharabasy','male')
member_two=membeerr('mohammed','nasser','saad','mal')
member_three=membeerr('sara','mahmoud','zain','femele')         

membeerr.show_users_count()

print("*"*50)
membeerr.sayhello()


#static method
      #1-can't takes no parameter
      #نستخمها لما نبق عايزين ننفذ حاجه من غبر مناكسس حاجه على الكلاس

