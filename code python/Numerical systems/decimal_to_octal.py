
def decimalToOctal(num):
    octalNum = [0] * 100

    counter = 0
    while (num != 0):
        octalNum[counter] = num % 8
        num = int(num / 8)
        counter += 1 
    for j in range(counter- 1, -1, -1):
        print(octalNum[j], end="")

number = 33
decimalToOctal(number)