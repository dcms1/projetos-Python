import random
import os

os.system("cls")
numero_sorteado=random.randrange(0,100)
erros=0
print("Jogo acerte o numero ") 
numero_usuario=int(input("Entre com o Numero: "))

while (numero_sorteado != numero_usuario):
    os.system('cls')
    if(numero_sorteado>numero_usuario):
        print("Erro,numero desejado e MAIOR")
    elif (numero_sorteado<numero_usuario): 
        print("Erro,numero desejado e MENOR")
    erros+=1
    numero_usuario=int(input("Entre com um novo: "))
print("Parabens voce acertou o numero: "+ str(numero_sorteado)+", em "+ str(erros+1))

    

