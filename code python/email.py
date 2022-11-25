name=input("enter your name: ").strip().capitalize()
password =input("enter your password: ").strip()
username=password[:password.index("@")]
website=password[password.index("@")+1:]

print(f"your name is {name} , your password is {password}")
print(f"your username is:{username} and the web site is {website}")