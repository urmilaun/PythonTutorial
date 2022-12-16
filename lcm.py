number1 = 23
number2 = 12
if(number1 > number2):
    maxValue = number1
else:
    maxValue = number2
while(True):
    if(maxValue % number1 == 0 and maxValue % number2 == 0):
        print("The LCM of the given two numbers",
              number1, ",", number2, "=", maxValue)
        break
    maxValue = maxValue + 1