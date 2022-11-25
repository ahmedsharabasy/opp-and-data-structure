def re_value(number):
    if (number>=0 and number<=9):
        return chr(number+ord('0'))
    else:
        return chr(number-10+ord('B')) 

def reverse_string(str):
    l=len(str)
    for i in range(int(l/2)):
        temp = str[i]
        str[i] = str[l - i - 1]
        str[l - i - 1] = temp

def fromdecimal(num,base):
    result=''
    while num>0:
        result +=re_value(num % base)
        num = int(num/base)

    result = result[::-1]        #تجميع لاارقام
    return result

num=input('Enter decimal number to be converted:')
base=input('Enter the base number:')
fromdecimal(num,base)        

    

