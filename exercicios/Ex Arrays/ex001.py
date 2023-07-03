from random import randint

oddnum = sorted([randint(0,50) for x in range(20) if randint(0,50) % 2 > 0])
print(oddnum)