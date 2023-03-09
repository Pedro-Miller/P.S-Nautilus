#listas com notas 1, 2 e 3 dos alunos de 0 a 10
notas1 = [6, 4, 8, 7, 7, 2, 8, 9, 5, 4]
notas2 = [4, 7, 8, 7, 3, 9, 7, 10, 7, 9]
notas3 = [10, 7, 3, 7, 9, 6, 7, 9, 9, 6]
alunos = ["aluno1", "aluno2", "aluno3", "aluno4", "aluno5", "aluno6", "aluno7", "aluno8", "aluno9", "aluno10"]

#função que soma as 3 notas dos alunos um a um e pprinta quais foram aprovados
def lista_resultados(listnotas1, listnotas2, listnotas3, listalunos):
    for i in range(10):
        aux = (listnotas1[i] + listnotas2[i] + listnotas3[i])/3
        if aux >=7:
            print(listalunos[i],":Aprovado")
        else:
            print(listalunos[i],":Reprovado")

lista_resultados(notas1, notas2, notas3, alunos)