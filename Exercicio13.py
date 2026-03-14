# Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.

salario= float(input('Digite o salário atual do funcionário: '))
aumento= float(input('Digite a % que o funcionário irá receber de aumento: '))

novoSalario= salario + (salario * aumento / 100)

print(f'O novo salário do funcionário será: {novoSalario:.2f}')