import time

tempo = 30
metodo = True

while True:
    print(tempo)
    tempo += 1 if metodo else -1
    time.sleep(1)
