#Atividade 2 de Kislansky

dados = [
    ("Marcelo", 8),
    ("Caio", 7),
    ("Manuele", 9.4),
    ("Welbert", 9),
    ("Pedro", 10),
    ("Kislansky", 7.5)
]

notas = {}

for item in dados:
    nome = item[0]
    nota = item[1]

    if nome in notas:
        notas[nome].append(nota)
    else:
        notas[nome] = [nota]

medias = {}

for aluno in notas:
    soma = 0
    quantidade = 0

    for nota in notas[aluno]:
        soma += nota
        quantidade += 1

    media = soma / quantidade
    medias[aluno] = media

lista_medias = []

for aluno in medias:
    lista_medias.append([aluno, medias[aluno]])

for i in range(len(lista_medias)):
    for j in range(i + 1, len(lista_medias)):
        if lista_medias[i][1] > lista_medias[j][1]:
            temp = lista_medias[i]
            lista_medias[i] = lista_medias[j]
            lista_medias[j] = temp

for item in lista_medias:
    aluno = item[0]
    media = item[1]
    print(aluno, "-", media)
