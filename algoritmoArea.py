def calcular_area_comodos(): # define uma função que calcula a area do comodo
    total_area = 0 # variavel area total recebe inicia com o valor 0
    return total_area # retorna a area total

while True: #enquanto verdadeiro
    largura = float(input("Digite a largura do cômodo (em metros): "))  # pede ao usuário para escrever a largura do comodo (float -> real)
    comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) # pede ao usuário apra escrever o comprimento do comodo (floar -> real)

area_comodo = largura * comprimento  # calculo para area do comodo -> recebe largura vezes o comprimento
print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") # mostra a area do comodo em metros

total_area += area_comodo

mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() # pergunta ao usuário se ele deseja adicionar mais comodos
if mais_comodos != 's': #se a resposta for diferente de "s"(ou seja, se o usuário não quer adicionar mais comodo)
    break  # break está fora do loop
    area_total = calcular_area_comodos() # variavel area_total recebe calcular_area_comodos vazio

    print(f"A área total da casa é: {area_total:.2f} metros quadrados.")  # finaliza mostrando ao usuário a area total da casa

