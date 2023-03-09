#pede as 3 notas do aluno
nota1 = int(input("Digite a primeira nota \n"))
nota2 = int(input("Digite a segunda nota \n"))
nota3 = int(input("Digite a terceira nota \n"))

#verifica se a média é necessária para passar e dá o resultado
if(nota1 + nota2 + nota3)/3 >=7:
    print('Aprovado')
else:
    print('Reprovado')
