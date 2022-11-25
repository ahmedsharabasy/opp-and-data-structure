def decimalToBinary(n):  
    if(n > 1):  
        decimalToBinary(n//2)  
    print(n%2, end=' ') 

if __name__ == '__main__': 
    number=int(input("Enter number to be converted to binary: ")) 
    print( decimalToBinary(number))