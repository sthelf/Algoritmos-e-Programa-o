# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

comprador = int(input(""))
compra = float(input(""))

cliente = compra 
funcionario = compra - (compra * 0.13)
premium = compra - (compra * 0.07)


if comprador == 1:
  print("Valor total a ser pago: R$%.2f" %(cliente))
elif comprador == 2:
  print("Valor total a ser pago: R$%.2f" %(funcionario))
elif comprador == 3:
  print("Valor total a ser pago: R$%.2f" %(premium))
else:
  print("OPÇÃO INVÁLIDA!") 