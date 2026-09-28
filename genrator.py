def genrator(max):
    count = 3
    while count>= max:
        yield count
        count-=1


counter = genrator(1)
for i in counter:
    print(i)



