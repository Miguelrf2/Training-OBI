quota_mensal = input('Quota mensal: ');
meses = input('Meses: ');

try:
    int(meses) + 1;
    int(quota_mensal) + 1;
except TypeError:
    print("Insira um número inteiro!")

saldo = 0

for i in range(1, int(meses) + 2):
    saldo += int(quota_mensal)

    if i == int(meses) + 1:
        break

    gastou = input(f'Gastou no mês {i}: ')

    try:
        int(gastou);
    except TypeError:
        print("Insira um número inteiro!")

    saldo -= int(gastou)

print(saldo)