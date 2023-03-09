#faz uma lista com os números menores que 1000
numeros = list(range(1000))
primos = []

#função que checa se o número é primo ou não excluindo numeros menores que 2 e checando se há divisores que não sejam 1 e ele mesmo
def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#gerando a lista de primos menores que 1000
for n in numeros:
    if primo(n) == True:
        primos.append(n)

#somando todos os numeros da lista
print(sum(primos))
    

    
