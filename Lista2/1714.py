# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

produto = float(input(""))

if produto < 20:
    valorVenda = produto * 1.45
    print("Valor de Venda: R$%.2f" % (valorVenda))
else:
    valorVenda = produto * 1.30
    print("Valor de Venda: R$%.2f" % (valorVenda))