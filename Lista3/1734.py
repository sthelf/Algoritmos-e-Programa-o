# Url do enunciado: 
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input(""))
x = 1
count = 1

while count <= n:
  x = x * count
  count = count + 1
print("%i!" %(n), "= %i" %(x))