idade=int(input("Qual a sua idade? \n"))

if idade <= 0:
    print("Idade incorreta")

elif idade < 18:
    print("Você é criança")

elif idade <= 65:
    print("Você é adulto")

else:
    print("Você é idoso")
