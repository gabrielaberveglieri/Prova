    def calcular_imc(peso, altura): # define uam funcao calcular imc com peso e altura

    imc = peso / (altura * 2) # imc recebe peso divido pela altura vezes 2
        return imc #retorna variavel imc

    def classificar_imc(imc):  #definie uma funcao classificar imc

if imc < 18.5: # se o imc for menor a 18.5
    return "Abaixo do peso"
elif 18.5 <= imc < 24.9: # se o imc for menor ou igual a 18.5, imc for menor que 24.9
    return "Peso normal"
elif 25 <= imc < 29.9: # se o imc for menor ou igual a 25, imc menor que 29.9
    return "Sobrepeso"
elif 30 <= imc < 34.9: # se o imc for menor ou igual a 30, imc menor a 34.9
    return "Obesidade grau 1"
elif 35 <= imc < 39.9: # se o imc for menor ou igual a 35 e maior menor que 39.9
    return "Obesidade grau 2"
else:
    return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc): #define outra funcao de sugestao de atividade fisica com base na classificacao

if classificacao_imc == "Abaixo do peso":  # condicoes definidias que irão mudar de acordo com a classificacao do imc
    return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
elif classificacao_imc == "Peso normal":
    return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve enatação, junto a um treino de força moderado."
elif classificacao_imc == "Sobrepeso":
    return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
elif classificacao_imc == "Obesidade grau 1":
    return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a umprograma de reeducação alimentar."
elif classificacao_imc == "Obesidade grau 2":
    return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
else:  # se não for nenhuma das outras opções, ele retorna a mensagem abaixo
return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

peso = float(input("Digite seu peso (em kg): "))  # pede para digir o peso em kg
altura = float(input("Digite sua altura (em metros): ")) # pede para digitar a altura em metros

imc = calcular_imc(peso, altura) # variavel imc recebe a funcao calcular_imc com peso e altura
classificacao_imc = classificar_imc(imc) #classificacao imc
sugestao = sugestao_atividade_fisica(classificacao_imc) #sugestao com base na classificacao do imc

print(f"Seu IMC é: {imc:.2f}")  # mostra o valor do imc
print(f"Classificação: {classificacao_imc}") # mostra a classificacao
print(f"Sugestão de atividade física: {sugestao}") # mostra a sugestão