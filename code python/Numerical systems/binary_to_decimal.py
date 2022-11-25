def binaryToDecimal(binary):      
    decimal=0
    counter=0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, counter) 
        binary = binary//10
        counter += 1
    print(decimal)     
      
if __name__ == '__main__': 
    binaryToDecimal(100) 
  