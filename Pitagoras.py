from math import isqrt
import sys
n=int(input("Digite o valor do primeiro cateto.\n"))
if n <= 0:
    print("Valor inválido.")
    sys.exit()
b=int(input("Digite o valor do segundo cateto. \n"))
if b <= 0:
    print("Valor inválido.")
    sys.exit()

z=n*n
c=b*b
v=z+c
j=isqrt(v)
print(j, "é o valor da hipotenusa.")