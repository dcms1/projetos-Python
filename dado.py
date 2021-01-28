import random
import os
continuar="s"
continuar=input(str("DESEJA JOGAR DADOS [s/n] \n"))

while continuar=="s":
    numero=random.randrange(0,6)
    print(numero)
    continuar=input(str("DESEJA JOGAR DADOS [s/n] \n"))
    if continuar=="n":
        print("Saindo do progrma")
        pass
    pass