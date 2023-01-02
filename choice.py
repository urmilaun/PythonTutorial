class MyException(Exception):
    Message=""
    def __init__(self,mg):
        self.Message=mg
try:
    age=int(input("Enter Age"))
    if(age>=21 and age<=30):
        print("Accepted")
    else:
        raise MyException("You are not eligible")

except MyException as m:
    print(m.Message)