# Leia 3 notas (float) e imprima a média com duas casas decimais.

n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite sua segunda nota: '))
n3= float(input('Digite sua terceira nota: '))

media= (n1+n2+n3)/3

print(f'A média das suas notas é: {media:.2f}')