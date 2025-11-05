import random

# -------------------------------
# CONFIGURAÇÕES DO ALGORITMO
# -------------------------------
TAMANHO_POP = 10       # número de indivíduos na população
GERACOES = 20           # número de gerações
TAXA_MUTACAO = 0.1      # 10% de chance de mutação
LIMITE_INFERIOR = -10
LIMITE_SUPERIOR = 10

# -------------------------------
# FUNÇÃO DE APTIDÃO (fitness)
# -------------------------------
def fitness(x):
    """Calcula a aptidão de um indivíduo (quanto maior, melhor)."""
    return x ** 2

# -------------------------------
# INICIALIZAÇÃO
# -------------------------------
def gerar_individuo():
    """Cria um indivíduo aleatório entre os limites."""
    return random.uniform(LIMITE_INFERIOR, LIMITE_SUPERIOR)

def gerar_populacao():
    """Cria a população inicial."""
    return [gerar_individuo() for _ in range(TAMANHO_POP)]

# -------------------------------
# SELEÇÃO (roleta viciada)
# -------------------------------
def selecionar_pais(populacao):
    """Seleciona um indivíduo com base na probabilidade proporcional ao fitness."""
    soma_fitness = sum(fitness(x) for x in populacao)
    pick = random.uniform(0, soma_fitness)
    atual = 0
    for x in populacao:
        atual += fitness(x)
        if atual >= pick:
            return x

# -------------------------------
# CROSSOVER (reprodução)
# -------------------------------
def crossover(pai1, pai2):
    """Gera um filho combinando os dois pais."""
    alfa = random.random()  # peso aleatório entre 0 e 1
    filho = alfa * pai1 + (1 - alfa) * pai2
    return filho

# -------------------------------
# MUTAÇÃO
# -------------------------------
def mutacao(individuo):
    """Aplica uma pequena perturbação ao indivíduo."""
    if random.random() < TAXA_MUTACAO:
        perturbacao = random.uniform(-1, 1)
        individuo += perturbacao
        # Garante que o valor fique nos limites
        individuo = max(min(individuo, LIMITE_SUPERIOR), LIMITE_INFERIOR)
    return individuo

# -------------------------------
# EXECUÇÃO PRINCIPAL
# -------------------------------
populacao = gerar_populacao()

for geracao in range(GERACOES):
    # Avalia população
    avaliacoes = [fitness(x) for x in populacao]
    
    # Mostra melhor da geração
    melhor_individuo = populacao[avaliacoes.index(max(avaliacoes))]
    print(f"Geração {geracao+1}: Melhor x = {melhor_individuo:.4f}, f(x) = {fitness(melhor_individuo):.4f}")
    
    # Nova população
    nova_populacao = []
    for _ in range(TAMANHO_POP):
        # Seleciona dois pais
        pai1 = selecionar_pais(populacao)
        pai2 = selecionar_pais(populacao)
        # Cria filho
        filho = crossover(pai1, pai2)
        filho = mutacao(filho)
        nova_populacao.append(filho)
    
    populacao = nova_populacao

# -------------------------------
# RESULTADO FINAL
# -------------------------------
melhor = max(populacao, key=fitness)
print("\nMelhor indivíduo final:")
print(f"x = {melhor:.4f}, f(x) = {fitness(melhor):.4f}")
