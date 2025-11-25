import random

# -------------------------------
# CONFIGURAÇÕES DO ALGORITMO
# -------------------------------
TAMANHO_POP = 4        # agora a população tem 4 indivíduos
GERACOES = 20
TAXA_MUTACAO = 0.1

# -------------------------------
# POPULAÇÃO INICIAL (sua matriz)
# -------------------------------
populacao = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# -------------------------------
# FUNÇÃO DE APTIDÃO (fitness)
# -------------------------------
def fitness(individuo):
    """Exemplo: soma dos genes (quanto maior, melhor)."""
    return sum(individuo)

# -------------------------------
# SELEÇÃO (roleta)
# -------------------------------
def selecionar_pais(pop):
    soma = sum(fitness(ind) for ind in pop)
    pick = random.uniform(0, soma)
    atual = 0

    for ind in pop:
        atual += fitness(ind)
        if atual >= pick:
            return ind

# -------------------------------
# CROSSOVER (1 ponto)
# -------------------------------
def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1)-1)
    filho = pai1[:ponto] + pai2[ponto:]
    return filho

# -------------------------------
# MUTAÇÃO
# -------------------------------
def mutacao(individuo):
    for i in range(len(individuo)):
        if random.random() < TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]  # alterna 0 ↔ 1
    return individuo

# -------------------------------
# EXECUÇÃO PRINCIPAL
# -------------------------------
for geracao in range(GERACOES):

    # avalia população
    avaliacoes = [fitness(ind) for ind in populacao]

    # mostra melhor
    melhor = populacao[avaliacoes.index(max(avaliacoes))]
    print(f"Geração {geracao+1}: Melhor = {melhor}, fitness = {fitness(melhor)}")

    nova = []
    for _ in range(TAMANHO_POP):
        pai1 = selecionar_pais(populacao)
        pai2 = selecionar_pais(populacao)
        filho = crossover(pai1, pai2)
        filho = mutacao(filho)
        nova.append(filho)

    populacao = nova

# -------------------------------
# RESULTADO FINAL
# -------------------------------
melhor_final = max(populacao, key=fitness)
print("\nMelhor indivíduo final:", melhor_final)
print("Fitness final:", fitness(melhor_final))
