# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

valAcum = 0

qtdNumero = int(input(""))

if qtdNumero <=0:
  print("Informe uma quantidade > 0!")
else:
  while qtdNumero > 0:
    informNumero = float(input(""))
    valAcum = valAcum + informNumero
    qtdNumero = qtdNumero -1
  print("Soma dos números informados: %.2f" %(valAcum))