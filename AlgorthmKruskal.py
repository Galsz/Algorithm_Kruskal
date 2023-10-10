import heapq

def union(conjuntos, set_ids, v1, v2):
    """Une os conjuntos que contêm v1 e v2."""
    set_id_v1, set_id_v2 = set_ids[v1], set_ids[v2]

    # Unindo o conjunto menor ao maior para otimizar
    if len(conjuntos[set_id_v1]) < len(conjuntos[set_id_v2]):
        set_id_v1, set_id_v2 = set_id_v2, set_id_v1

    for vertice in conjuntos[set_id_v2]:
        set_ids[vertice] = set_id_v1
        conjuntos[set_id_v1].append(vertice)

    conjuntos[set_id_v2] = []

# 1. Ler número de vértices e arestas
num_vertices, num_arestas = map(int, input("Digite o número de vértices e arestas: ").split())

# 2. Ler as arestas e seus respectivos pesos, e armazená-los em um heap
arestas = []
for _ in range(num_arestas):
    v1, v2, peso = map(int, input(f"Digite a aresta (formato: vértice1 vértice2 peso): ").split())
    heapq.heappush(arestas, (peso, v1, v2))

# 3. Inicialização: Criar conjuntos disjuntos
conjuntos = [[i] for i in range(num_vertices)]
set_ids = [i for i in range(num_vertices)]

# 4. Algoritmo de Kruskal
custo_total = 0
print("\nProcesso de construção da árvore geradora mínima:\n")

while arestas:
    peso, v1, v2 = heapq.heappop(arestas)
    
    if set_ids[v1] != set_ids[v2]:  # Verifica se estão em conjuntos diferentes
        print(f"Aresta {v1}-{v2} de peso {peso} foi adicionada.")
        custo_total += peso
        union(conjuntos, set_ids, v1, v2)
    else:
        print(f"Aresta {v1}-{v2} de peso {peso} foi ignorada (formaria ciclo).")

print(f"\nCusto total da árvore geradora mínima: {custo_total}")


# Entrada de dados, vertices e arestas
# V A C
# 9 14
# 0 1 4
# 0 7 8
# 1 2 8
# 1 7 11
# 2 3 7
# 2 5 4
# 2 8 2
# 3 4 9
# 3 5 14
# 4 5 10
# 5 6 2
# 6 7 1
# 6 8 6
# 7 8 7 
# Árvore geradora de custo 37