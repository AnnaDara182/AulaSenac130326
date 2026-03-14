# Leia um número como string e imprima o seu tipo antes e depois de converter para int.

numero_str= str(input('Digite um numero: '))

print('Antes da conversão:', type(numero_str))

numero_int= int(numero_str)

print('Depois da conversão:', type(numero_int))