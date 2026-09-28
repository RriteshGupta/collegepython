def double_result(fun):
    def waraper():
        print("function caling")
        fun()
        return waraper


@double_result
def sum():
    print(sum)

sum()
