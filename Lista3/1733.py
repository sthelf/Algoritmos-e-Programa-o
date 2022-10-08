# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

salMinimo = 1192.40
valHoraExtra = 10.00

NomeFunc = input ("")
horaExtra = float (input(""))

salHoraExtra = horaExtra * valHoraExtra
salBruto = 3 * salMinimo + salHoraExtra


if salBruto > 2000.00:
  INSS = salBruto * 0.12
else:
  INSS = salBruto * 0.05

if salBruto > 2500.00:
  IR = salBruto * 0.20
else:
  IR = 0

salLiquido = salBruto - INSS - IR


print ("Nome: %s" %(NomeFunc))
print ("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" % (salLiquido))