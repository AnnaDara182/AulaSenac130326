# Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)

tempo = int(input("Digite a quantidade de minutos: "))

horas = tempo // 60
minutos = tempo % 60

print(horas, 'horas e', minutos, 'minutos')