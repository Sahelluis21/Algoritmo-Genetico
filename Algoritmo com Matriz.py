import random

# -------------------------------
# CONFIGURAÇÕES
# -------------------------------
TAM_POP = 4
GERACOES = 20
TAXA_MUT = 0.1

# -------------------------------
# POPULAÇÃO INICIAL
# -------------------------------
pop = [
    
    (1, 0, 1, 0, 1, 1, 0, 1, 0, 0),
    (0, 1, 1, 1, 0, 0, 1, 0, 1, 1),
    (1, 1, 0, 0, 1, 0, 0, 1, 0, 1),
    (0, 0, 1, 0, 1, 1, 1, 0, 0, 0),
    (1, 0, 1, 1, 0, 0, 0, 1, 1, 0),
    (0, 1, 0, 1, 1, 1, 0, 0, 1, 1),
    (1, 0, 1, 0, 0, 1, 1, 1, 0, 0),
    (0, 1, 0, 1, 0, 1, 1, 0, 1, 1),
    (1, 1, 0, 0, 1, 0, 1, 1, 0, 0),
    (0, 0, 1, 1, 0, 1, 0, 0, 1, 1)

]

# -------------------------------
# FITNESS
# -------------------------------
def fitness(ind):
    return sum(ind)

# -------------------------------
# SELEÇÃO POR TORNEIO (mais rápido)
# -------------------------------
def torneio(pop):
    a, b = random.sample(pop, 2)
    return a if fitness(a) > fitness(b) else b

# -------------------------------
# CROSSOVER 1 PONTO
# -------------------------------
def crossover(p1, p2):
    ponto = random.randint(1, len(p1) - 1)
    return p1[:ponto] + p2[ponto:]

# -------------------------------
# MUTAÇÃO
# -------------------------------
def mutacao(ind):
    ind = list(ind)
    for i in range(len(ind)):
        if random.random() < TAXA_MUT:
            ind[i] = 1 - ind[i]
    return tuple(ind)

# -------------------------------
# LOOP PRINCIPAL
# -------------------------------
for g in range(GERACOES):

    # fitness calculado apenas 1x!
    fit_values = [fitness(i) for i in pop]

    melhor = pop[fit_values.index(max(fit_values))]
    print(f"Geração {g+1}: melhor={melhor}, fit={fitness(melhor)}")

    nova = []
    for _ in range(TAM_POP):
        p1 = torneio(pop)
        p2 = torneio(pop)
        filho = crossover(p1, p2)
        filho = mutacao(filho)
        nova.append(filho)

    pop = nova

# -------------------------------
# RESULTADO FINAL
# -------------------------------
melhor_final = max(pop, key=fitness)
print("\nMelhor indivíduo final:", melhor_final)
print("Fitness final:", fitness(melhor_final))
