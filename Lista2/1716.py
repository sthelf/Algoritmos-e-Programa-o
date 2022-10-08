# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input("")
salario = float(input(""))

salarioPlanoA = salario + (salario * 0.10)
salarioPlanoB = salario + (salario * 0.15)
salarioPlanoC = salario + (salario * 0.20)

if plano == "A":
  print("Novo salário: R$%.2f" %(salarioPlanoA))
elif plano == "B":
  print("Novo salário: R$%.2f" %(salarioPlanoB))
elif plano == "C":
  print("Novo salário: R$%.2f" %(salarioPlanoC))