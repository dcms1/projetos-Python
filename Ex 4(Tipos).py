someThing=input("Entre com alguma coisa: ")
print("O tipo de que voce entrou e ",type(someThing),end=", ")
print("So tem espaco ",someThing.isspace(),end=", ")
print('E um numero ',someThing.isnumeric(),end=", ")
print('Sao letras ',someThing.isalpha(),end=", ")
print('E alphanumerico',someThing.isalnum(),end=", ")
print('Esta com letras maiusculas ',someThing.isupper(),end=", ")
print('Esta com letras minusculas ',someThing.islower(),end=", ")
print('Esta capitalizado ',someThing.title(),end=", ")

