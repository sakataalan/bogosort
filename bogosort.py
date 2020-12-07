import time
import random


lista = []

print(file=open("test.txt", "w"))

for i in range(1, 9):
    lista.append(i)

random.shuffle(lista)

inicio = time.time()
def bogosort(seq):
    while not all(x <= y for x, y in zip(seq, seq[1:])):
        random.shuffle(seq)
        print(seq, file=open("test.txt", "a"))
    return seq

print('Hora do show porra')
bogosort(lista)
print(lista)
fim = time.time()
tempo = (fim - inicio) / 60
print(f'{round(tempo, 2)}')
