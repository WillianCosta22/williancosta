#Atividade 3 de Kislansky

produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

medias = {}

for categoria in produtos:

    soma = 0
    quantidade = 0

    for preco in produtos[categoria]:
        soma += preco
        quantidade += 1

    media = soma / quantidade
    medias[categoria] = media

maior = 0
categoria_vencedora = ""

for categoria in medias:
    if medias[categoria] > maior:
        maior = medias[categoria]
        categoria_vencedora = categoria

print("Categoria mais cara:", categoria_vencedora)
print("Média:", round(maior, 2))
