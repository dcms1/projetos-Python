n1 = int (input("entre com um numero: "))
n2 = int (input("entre com um outro numero: "))
s1 = input("entre com uma operacao: ")

if s1 == "+":
    res = n1+n2
    print(n1, "+", n2, "=", res)
elif s1 == "-":
    res = n1-n2
    print(n1, "-", n2, "=", res)
elif s1 == "/":
    res = n1/n2
    print(n1, "/", n2, "=", res)
elif s1 == "*" :
    res = n1*n2
    print(n1,"*",n2,"=",res)
else:
    print("operaçao nao encontrada")