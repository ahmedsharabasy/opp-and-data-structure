from model import person
def show_all_view(list):
    print("in our db we have %i users. Here they are: %len(list)")
    for item in list:
        print(item.name())

def start_view():
    print("MVc - the simplest examble")
    print("do you wont to see every one in my db?[y/n]")

def end_view():
    print("goodbye")            

