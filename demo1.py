class BEStudent:
    def details(self):
        print("BE Student Called")

    def profile(self):
        print("BE Student Profile")

class BCAStudent:
    def details(self):
        print("BCA Student Called")

    def profile(self):
        print("BCA Student Profile")

def call(obj):
    obj.details()
    obj.profile()

be=BEStudent()
bca=BCAStudent()
call(be)
call(bca)