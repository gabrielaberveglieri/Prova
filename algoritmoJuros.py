def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): #define uma função que irá calcular os juros em atraso
    return valor_total, juros  # retorna o valor total e juros

taxa_juros_diaria = taxa_juros_anual / 365 / 100  # a taxa de juros diaria receb a taxa de juros anual dividido por 365 (dias nao), dividido por 100


juros = valor_principal * taxa_juros_diaria * dias_atraso # variavel juros recebe o valor principal * a taxa de juros * dias em atraso

valor_total = valor_principal + juros  # variavel valor_total recebe o valor principal somado aos juros


valor_principal = 1000.00  # define um valor para variavel
taxa_juros_anual = 5.0 # define um valor para a variavel
dias_atraso = 30 # define um valor para a variavel
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
print(f"Valor total a ser pago: R${valor_total:.2f}") # mostra para o usuário o valor a ser pago
print(f"Valor dos juros: R${juros:.2f}") # mostra ao usuário o valor dos juros