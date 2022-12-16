def findGcd(number1, number2):
    if number1 > number2:
        smallNumber = number2
    else:
        smallNumber = number1
    
    for i in range(1, smallNumber+1):
      
        if((number1 % i == 0) and (number2 % i == 0)):
            result = i
    
    return result

number1 = 24
number2 = 36
ans = findGcd(number1, number2)
print("The Highest Common Factor (HCF) of the numbers", number1, number2, "=", ans)