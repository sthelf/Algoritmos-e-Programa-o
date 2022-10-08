# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

inicio = int(input(""))
fim = int(input(""))

contagem = 1

while contagem <= inicio and inicio >= fim:
  print(inicio)
  inicio = inicio - contagem
  
print("Fogo!")