# Durações dos episódios
duracoes = [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]

# Calculando a média
media = sum(duracoes) / len(duracoes)

print("A média das durações dos episódios é:", media, "minutos")

# Durações dos episódios
duracoes = [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]

# Ordenando a lista de durações
duracoes_ordenadas = sorted(duracoes)

# Se o número total de elementos for ímpar
if len(duracoes_ordenadas) % 2 != 0:
    mediana = duracoes_ordenadas[len(duracoes_ordenadas) // 2]
else:  # Se o número total de elementos for par
    mediana = (duracoes_ordenadas[len(duracoes_ordenadas) // 2 - 1] + duracoes_ordenadas[len(duracoes_ordenadas) // 2]) / 2

print("A mediana das durações dos episódios é:", mediana, "minutos")

from collections import Counter

# Durações dos episódios
duracoes = [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]

# Contando a frequência de cada duração
contagem_duracoes = Counter(duracoes)

# Encontrando a(s) moda(s)
moda = contagem_duracoes.most_common(1)

# Se houver mais de uma moda (várias durações com a mesma frequência máxima)
if len(moda) > 1:
    modas = [moda[0][0]]
    for i in range(1, len(moda)):
        if moda[i][1] == moda[0][1]:
            modas.append(moda[i][0])
else:
    modas = [moda[0][0]]

print("A(s) moda(s) das durações dos episódios é(são):", modas)


# Número de chaves de fenda
num_chaves_fenda = 4

# Número total de chaves
num_total_chaves = 4 + 3  # 4 chaves de fenda + 3 chaves Philips

# Calculando a probabilidade
probabilidade = num_chaves_fenda / num_total_chaves

print("A probabilidade de pegar uma chave de fenda é:", probabilidade)
