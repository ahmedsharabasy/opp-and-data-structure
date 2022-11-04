class food:
    def __init__(self,name):       #base class
        self.name=name
        print(f"{self.name} is ready")

    def eat(self):
        print("eat methtod from base class")


class Apple(food):      #derived class
    def __init__(self,name):
        food.__init__(self,name)     #create instance from base class 
        super().__init__(name)       #شبه السطر الى فوق ده
        print(f"{self.name} method created from derived class")        



food1=food("pizza")
food2=Apple("app")
food2.eat()