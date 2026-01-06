import sys
n=int(input("Escolha um número inteiro positivo como limite dos números.\n"))
if n <= 0:
    print("Número inválido")
    sys.exit()

p=int(input("Escolha um número inteiro positivo pra ser o divisor desses números.\n"))
if p <= 0:
    print("Número inválido")
    sys.exit()

for i in range(1, n+1):
    if i % p == 0:
        print(i,"é divisível")
    else:
        print(i)