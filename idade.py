nomes = [
    input('Cibele: '),
    input('Camila: '),
    input('Celeste: ')
]

numeros = []

for i in nomes:
    try:
        int(i) + 1
        numeros.append(i)
    except ValueError:
        print("Forneça um número inteiro.")


lista_decrescente = sorted(numeros, reverse=True)

print(f'Camila tem {lista_decrescente[-2]} anos')