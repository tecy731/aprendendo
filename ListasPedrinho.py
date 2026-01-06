import sys
n=[]
for a in range(5):
    a=int(input("Escolha um número inteiro positivo. \n"))
    if a <= 0:
        print("Número inválido")
        sys.exit()
    n.append(a)
    print(n)

for b in n:
    if b % 2 == 0:
        print(b, "é par")
    else:
        print(b, "é ímpar")

x=0
d=None

for z in n:
    if z > x:
        x=z
print(x, "é o maior número")

for z in n:
    if d == None:
        d=z
    if z < d:
        d=z
print(d, "é o menor número")