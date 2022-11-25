#module is file contain a set of functions
#import module in your app to help you 
#can import multiple modules
#can create your own module
#modules saves your time
#----------------------------------------------------

#import main module
import random
print(f"RANDOM FLOAT NUMBER  {random.random()}")



#show all fun in random

import random
print(dir(random))


import one or two functions from modulefrom random import randint
print(f"print random integer : {randint(100,900)}")


from random import randint,random
print(f"print random integer : {randint(100,900)}")
print(f"print random integer : {random()}")


import sys
print(sys.path)
sys.path.append("E:\\aaa.txt")
print(sys.path)


# import datetime
# print(datetime.datetime(2021,4,18))


# import math
# x = math.sqrt(64)
# print(x)



# import math
# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x) # returns 2
# print(y) # returns 1


# import math
# x = math.pi
# print(x)



