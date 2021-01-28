import math

a = float(input("Insira um valor para A: "))
b = float(input("Insira um valor para B: "))
c = float(input("Insira um valor para C: "))

d = b ** 2 - 4 * a * c
print("Delta: ", d)

if d > 0 :
    print("Delta positivo - 2 raizes")
    d = math.sqrt(d)
    print("Raiz quadrada de Delta: ")
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    print("As raizes sao",x1,"e",x2)
elif d == 0 :
    print("Delta igual a zero - 1 raiz")
    d = math.sqrt(d)
    print("Raiz quadrade de Delta: ")
    x3 = (-b + d) / (2 * a)
    print("As raizes sao ", x3)
else:
    print("Delta menor que zero - sem raizes reais possiveis ")