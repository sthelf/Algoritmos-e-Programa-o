# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

preco = 1
soma = 0
while preco != 0:
    preco = float(input())
    soma += preco
valor = float(input())
troco = valor - soma
print("Total da compra: R$%.2f" %(soma))
print("Valor pago: R$%.2f" %(valor))
print("Troco: R$%.2f" %(troco))