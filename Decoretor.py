def decoretor(fun):
    def waraper():
       print("Function Calling")

       fun()

       print("function End")
       return waraper
@decoretor
def my_function(a):
    return a*a

my_function(5)


