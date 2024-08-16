def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #define uma função para diagnosticar diabetes com base na glicemia em jejum e pos prandial

    # se a glicemia em jejum for maior ou igual à 126 OU glicemia pos prandial for maior ou igual à 200
    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        return "Diabetes"  # o paciente tem diabetes
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: # não entendi a lógica 
        return "Pré-diabetes"
    else: # se não for nenhum dos outros dois casos, retorna diabates "normal"
        return "Normal"

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) # pede ao usuário para digitar
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) # pede ao usuário para digitar

# variavel resultado recebe e guarda a funcao diagnosticar_diabetes
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
print(f"O diagnóstico é: {resultado}") #mostra o resultado do diagnóstico