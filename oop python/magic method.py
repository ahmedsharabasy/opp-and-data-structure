class skill:
    def __init__(self):
        self.skills=["C++","PYTHON","matlap"]
    def __str__(self):
        return f"this my skills {self.skills}"      #gives the human redable output of the object

    def __len__(self):
        return len(self.skills)    


profile=skill()
print(profile)
print(profile.__class__)
print(len(profile))


profile.skills.append("php")
print(len(profile))

# mystring="Ahmed"
# print(type(mystring))
# print(mystring.__class__)
# print(dir(str))  
# print(str.upper(mystring))              #magic method  هى كيفية الوصول الى الاوبجكت بدةن معرفة لكلاس مثلا وانا الى بعرف الكلاس 



print("*"*50)
##################################################################

