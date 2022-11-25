def hexadecimalToDecimal(hexval):  
    length = len(hexval) 
    base = 1
    decimal = 0
      
    for i in range(length - 1, -1, -1): 
        if hexval[i] >= '0' and hexval[i] <= '9': 
            decimal += (ord(hexval[i]) - 48) * base  
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F': 
            decimal += (ord(hexval[i]) - 55) * base 
            base = base * 16        
    return decimal 

if __name__ == '__main__':     
    hexnum = '7c'    
    print(hexadecimalToDecimal(hexnum)) 