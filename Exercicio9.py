# Leia o preço de um produto e imprima o preço com 10% de desconto.

valor= float(input('Informe o valor total do produto: '))

desconto= valor * 0.10
valorFinal= valor - desconto

print('Você recebeu 10% de desconto! O valor final é: ', valorFinal)