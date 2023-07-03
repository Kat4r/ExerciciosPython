tab = int(input('Digita o numero o qual deseja a tabuada: '))
for pos, num in enumerate(range(tab,tab * 11,tab)):
    print(f"{tab} x {pos+1} = {num}")