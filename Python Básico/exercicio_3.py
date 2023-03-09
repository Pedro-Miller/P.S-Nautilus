#cria uma lista com os numeros de 1 a 1000
numeros = list(range(1001))

pares = []
impares = []

#separa os pares e os impares verificando sua divisibilidade por 2
for i in numeros:
    if i%2!=0:
        impares.append(i)

print(pares)
print(impares)