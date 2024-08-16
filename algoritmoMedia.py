def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): # define uma função que irá calcular a media e aprovacao dos alunos
total_notas = 0 # variavel total_notas inicia em 0

num_alunos = len(notas) # a função "len" irá devolver o tamanho (número de itens) d eum objeto
aprovados = [] # lista de aprovados
reprovados = [] #lista de reprovados

    return media_turma, aprovados, reprovados

for aluno, nota in notas.items():
    total_notas += nota
if nota >= nota_minima_aprovacao: # se a variavel nota for maior ou igual a variavel "nota_minina_aprovacao)
    aprovados.append(aluno) # adiciona o item a lista de aprovados
else: # se não
    reprovados.append(aluno) # adiciona o item na lista de reprovados

media_turma = total_notas / num_alunos  # media turma recebe total de notas dividido pelo numero de alunos

notas = {"Alice": 85,"Bruno": 72,"Carlos": 60,"Diana": 95,"Eduardo": 55} # lista notas recebe os nomes dos alunos e as notas de cada um

nota_minima_aprovacao = 70  # define a variavel nota minima de aprovacao em 70

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

print(f"Média da turma: {media_turma:.2f}") #mostra ao usuário a média da turma, alunos aprovados e os reprovados
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")