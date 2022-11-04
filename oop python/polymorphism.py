#ميثود بتعمل حاجه فى مكان وهى هياها نفس الميثود بتعمل حاجه بس فى حته تانيه
#شبه الاوفررايد
n1=10
n2=20
print(n1+n2)

s1="hello"
s2="python"
print(s1+s2)
#####################################################################
print(len([1,2,3,4,5,6]))
print(len("hello Ahmed"))
print(len({"one":1,"two":2}))

#####################################################################

class A:
    def do_something(self):
        print("from class A")
        raise NotImplementedError("derived class must implement this method")   #لازم كل الكلاسز الى معمولها وراثه يتم وضع هذه الفانكشن فى داخلها


class B(A):
    def do_something(self):
        print("from class B")

my_instance=B()
my_instance.do_something()