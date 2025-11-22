#Atividade 1 de Kislansky

num_inteiros = [2, 3, 4, 5, 8, 11, 15, 17, 32, 49, 73, 94]

primos = []
nao_primos = []

for n in num_inteiros:
    if n < 2:
        nao_primos.append(n)
        continue

    eh_primo = True
    for i in range(2, n):
        if n % i == 0:
            eh_primo = False
            break

    if eh_primo:
        primos.append(n)
    else:
        nao_primos.append(n)

print("Números primos: ", primos)
print("Números não primos: ", nao_primos)
