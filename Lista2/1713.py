# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

salario = float(input(""))
horasTrabalhadas = float(input(""))

salarioBruto = (salario * horasTrabalhadas)
impostoRen = (salarioBruto * 0.11)
inss = (salarioBruto * 0.08)
sind = (salarioBruto * 0.05)
salarioLiq = (salarioBruto - impostoRen - inss - sind)

print(
    "Salário bruto: R$%.2f \nImposto: R$%.2f \nINSS: R$%.2f \nSindicato: R$%.2f \nLíquido: R$%.2f"
    % (salarioBruto, impostoRen, inss, sind, salarioLiq))