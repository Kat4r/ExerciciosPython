from random import  randint

numerosrand = [randint(0,1500) for x in range(100)]
c500 = 0
for n in numerosrand:
    if n < 500:
        c500 += 1

print(c500)