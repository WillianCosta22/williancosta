#Atividade 6 de Kislansky

from collections import Counter

frase = input("Digite uma frase: ")

contador = Counter(frase)

if len(contador) < 3:
    print("Não há caracteres suficientes.")
else:
    mais_comuns = contador.most_common(3)

    terceiro = mais_comuns[2]
    caractere = terceiro[0]
    quantidade = terceiro[1]

    print("3º mais frequente:", caractere)
    print("Aparece:", quantidade, "vezes")
