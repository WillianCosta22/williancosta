#Atividade 4 de Kislansky

A = [2, 3, 5]
B = [1, 4, 2]

if len(A) != len(B):
    print("Os vetores têm tamanhos diferentes!")
else:
    produto = 0
    i = 0
    while i < len(A):
        produto = produto + (A[i] * B[i])
        i += 1

    print("Produto escalar =", produto)
