numero=int(input('Entre com o valor em metros para a conversao: '))
numeroMM=numero * 1000
numeroCM=numero * 100
numeroDM=numero * 10
numeroDAM=numero * 0.1
numeroHM=numero * 0.01
numeroKM=numero * 0.001
print('O numero em MM: {}\n'
      'O numero em CM: {}\n'
      'O numero em DM: {}\n'
      'O numero em DAM: {}\n'
      'O numero em HM: {}\n'
      'O numero em KM: {}\n'.format(numeroMM,numeroCM,numeroDM,numeroDAM,numeroHM,numeroKM))