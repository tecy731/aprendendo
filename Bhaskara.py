from math import isqrt
import sys

a=int(input("Diga o valor de a.\n"))
b=int(input("Diga o valor de b.\n"))
c=int(input("Diga o valor de c.\n"))

j=(b*b)-4*a*c
if j <= 0:
    print(j, "é o valor de Delta. Delta sendo negativo, não será possível prosseguir.")
    sys.exit()

h=isqrt(j)

k=(-b+h)/(2*a)
p=(-b-h)/(2*a)

print(k, "é o valor de x'")
print(p, "é o valor de x''")
