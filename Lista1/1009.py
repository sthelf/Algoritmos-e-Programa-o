# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input("")
salario = float(input(""))
vendas = float(input(""))


TOTAL = (salario + (vendas * 0.15))

print("TOTAL = R$ %0.2f" %(TOTAL))