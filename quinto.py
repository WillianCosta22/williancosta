#Atividade 5 de Kislansky

valor = input("Digite um número: ")

try:
    numero = float(valor)

    if numero.is_integer():
        numero_int = int(numero)

        if numero_int % 2 == 0:
            print("É Inteiro e Par.")
        else:
            print("É inteiro e Ímpar.")
    else:
        parte_inteira = int(numero)
        parte_decimal = numero - parte_inteira

        print("É Decimal.")
        print("Parte Inteira:", parte_inteira)
        print("Parte Decimal:", parte_decimal)

except:
    print("Erro: valor digitado não é número!")
