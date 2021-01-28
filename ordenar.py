n1 = int (input("entre com um numero "))
n2 = int (input("entre com um numero diferente do primeiro "))
n3 = int (input("entre com um numero diferetente dos anteriores "))

lista = (n1,n2,n3)
print(sorted(lista, reverse=True))