# 1)Importando a biblioteca random para gerar números aleatórios
import random

# Gerando um conjunto de números inteiros aleatórios entre -10 e 20
conjunto_numeros = set(random.sample(range(-10, 21), 30))

# Verificando se o número -1 está no conjunto
if -1 in conjunto_numeros:
    print("-1 está presente no conjunto.")
else:
    print("-1 não está presente no conjunto.")


#2)# Importando a biblioteca random para gerar números aleatórios
import random

# Gerando um conjunto de números inteiros aleatórios entre -10 e 20
conjunto_numeros = set(random.sample(range(-10, 21), 30))

# Verificando se o número -11 está no conjunto
if -11 in conjunto_numeros:
    print("-11 está presente no conjunto.")
else:
    print("-11 não está presente no conjunto.")

#3)# Definindo o conjunto de salários mínimos
S = {100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510, 540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}

# Verificando se R$ 350,00 está presente no conjunto
if 350 in S:
    print("O valor R$ 350,00 está presente no conjunto.")
else:
    print("O valor R$ 350,00 não está presente no conjunto.")

#4)# Senhas criadas
senhas = {'452012', '323233', '787910', '528917', '683524'}

# Função para verificar a senha
def verificar_senha(senha):
    if senha in senhas:
        print("Acesso permitido!")
    else:
        print("Senha incorreta. Acesso negado.")

# Solicitar a senha ao usuário
senha_digitada = input("Digite a senha: ")

# Verificar a senha digitada
verificar_senha(senha_digitada)

#5)# Vetor de preços originais
v = (1210, 897, 1230, 1495, 799, 890, 1010)

# Calculando os preços com desconto de 20%
precos_com_desconto = [preco * 0.8 for preco in v]

# Imprimindo os preços com desconto
print("Preços com desconto de 20%:")
for preco in precos_com_desconto:
    print(preco)

# Vetores u e v
u = (3, 4, 8)
v = (10, 12, -1)

# Somando os vetores
u_v = tuple(u[i] + v[i] for i in range(len(u)))

# Imprimindo o resultado
print("O vetor u + v é:", u_v)

