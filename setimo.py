#Atividade 7 de Kislansky

livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]



anos = {}

for livro in livros:
    ano = livro["ano"]
    titulo = livro["titulo"]
    preco = livro["preco"]

    if ano not in anos:
        anos[ano] = {"titulos": [titulo], "soma": preco, "quant": 1}
    else:
        anos[ano]["titulos"].append(titulo)
        anos[ano]["soma"] += preco
        anos[ano]["quant"] += 1

lista_anos = list(anos.keys())

for i in range(len(lista_anos)):
    for j in range(i + 1, len(lista_anos)):
        if lista_anos[i] > lista_anos[j]:
            temp = lista_anos[i]
            lista_anos[i] = lista_anos[j]
            lista_anos[j] = temp


for ano in lista_anos:
    dados = anos[ano]
    media = dados["soma"] / dados["quant"]

    print("Ano:", ano)
    print("Livros:", dados["titulos"])
    print("Média:", round(media, 2))
    print()
