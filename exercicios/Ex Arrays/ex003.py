from random import  randint

numerosrand = [randint(0,1500) for x in range(100)]

for num in numerosrand:
    numQua = [num**2]
    print(numQua)