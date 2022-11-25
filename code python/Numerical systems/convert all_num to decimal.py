def re_value(number):
    if (number>='0' and number<='9'):
        return ord(number)-ord('0')
    else:
        return ord(number)-ord('A')+10 

def to_decimal(num,base):
    n=len(num)
    result=0
    power=0
    for i in range(n-1,-1,-1):
        if re_value(num[i]) >= base:
            return 'invalid number'
        else:
            result+=re_value(num[i])*pow(base,power)
            power+=1
    return result   

numb=input('Enter number to be converted to decimal:')
base=int(input('Enter the base of the number:'))
print(to_decimal(numb,base))

