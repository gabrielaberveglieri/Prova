def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):
    #define a variavel

custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel # variavel recebe a distancia dividido pelo consumo vezes o custo do combustivel

custo_pedagio_total = numero_pedagios * custo_pedagio # custo do combustiver total recebe o numero de pegadios vezes o custo do pedagio

custo_total = custo_combustivel_total + custo_pedagio_total # variavel custo total recebe o custo do combustiver total mais o custo do pedagio total

return custo_total, custo_combustivel_total, custo_pedagio_total # retorna o custo total, preco do combustivel total e custo total do pedagio

# essa parte irá pedir para o usuário inserir os valores para preencher todas as variáveis
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio)

# essa parte irá mostrar ao usuário o custo total da viagem, custo total com combustível e custo total com pedágios
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")