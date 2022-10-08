# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

idademaior = 0
idades = 0
for c in range(4):
    idade = int(input())
    idades += idade
    peso = float(input())
    if peso > 90:
        idademaior += 1

media = idades / 4
print("Qtd pessoas > 90 Kg: %.i" %(idademaior))
print("Idade média: %.2f" %(media))