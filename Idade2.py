import sys
try: 
    idade=int(input("Qual a sua idade?\n"))
except:
    print("Idade inválida, utilize algarismos.\n")
    sys.exit()

estuda=str(input("Você estuda? (sim/não)\n")).lower()

if idade <= 0:
    print("Idade incorreta")

elif idade < 18:
    if estuda=="sim":
        print("Você é jovem estudante")
    elif estuda=="não":
        print("Você é jovem e não estuda")
    else:
        print("Resposta inválida")

elif idade >= 18:
    if estuda=="sim":
        print("Você é adulto estudante")
    elif estuda=="não":
        print("Você é vagabundo")
    else:
        print("Resposta inválida")
