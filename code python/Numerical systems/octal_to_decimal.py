def octalToDecimal(num):     
    number = num; 
    decimal= 0; 
    base= 1; 
  
    temp = number; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10);  
        decimal += last_digit * base; 
        base = base * 8;   
    return decimal; 
 
num = 67; 
print(octalToDecimal(num)); 