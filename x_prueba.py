import random

puntaje = 0
dado_1 = 0
dado_2 = 0

while dado_1 != 1 and dado_2 != 1 and puntaje != 31:
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    puntaje = puntaje + dado_1 + dado_2
    print(dado_1, dado_2)
    print('Puntaje', puntaje)