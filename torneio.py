games = [
 input('Partida 1: ').lower(),
 input('Partida 2: ').lower(),
 input('Partida 3: ').lower(),
 input('Partida 4: ').lower(),
 input('Partida 5: ').lower(),
 input('Partida 6: ').lower()
]

derrotas = 0
vitorias = 0

for i in games:
    if i == 'v':
        vitorias += 1
    elif i == 'p':
        derrotas += 1

#filter

if vitorias == 5 or vitorias == 6:
    print('Grupo 1')

elif vitorias == 3 or vitorias == 4:
    print("Grupo 2")

elif vitorias == 1 or vitorias == 2:
    print("Grupo 3")

elif vitorias == 0:
    print(-1)