ex01_tupla.py
dias_uteis = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

print(dias_uteis[0])   # Segunda
print(dias_uteis[-1])  # Sexta
print(len(dias_uteis)) # 5

ex02_tupla.py
notas = (8, 3, 7, 5, 2, 9, 4)

for nota in notas:
    if nota >= 5:
        print(nota)

# Saída:
# 8
# 7
# 5
# 9

ex03_tupla.py
numeros = (4, 7, 2, 9, 1, 5)

print(numeros.count(7))  # 1
print(numeros.index(9))  # 3

ex04_tupla.py
temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for temp in temperaturas:
    if temp < 37.5:
        print("Normal")
    elif temp <= 38.5:
        print("Febre moderada")
    else:
        print("Febre alta")

# Saída:
# Normal
# Normal
# Febre moderada
# Normal
# Febre alta
