grafo = {
    'Mi Casa': ['Americas', 'Casa de Maria'],
    'Americas': ['chapu', 'Rakata'],
    'Casa de Maria': ['Kanna'],
    'chapu': [],
    'Rakata': ['Kanna'],
    'Kanna': []
}

# Función heurística: Distancia estimada desde un nodo al objetivo (en este caso, 'Kana')
def heuristica(nodo):
    if nodo == 'Kanna':
        return 0
    elif nodo == 'Rakata':
        return 1  # Distancia a 'Kana' es 1 desde 'Rakata'
    else:
        return float('inf')  # Infinito para nodos no explorados

# Algoritmo Greedy Best First Search
def greedy_best_first_search(grafo, inicio, objetivo):
    frontera = [(inicio, [inicio])]  # Inicializamos la frontera con el nodo inicial y la ruta
    visitados = set()  # Para evitar visitar el mismo nodo varias veces

    while frontera:
        nodo_actual, ruta_actual = frontera.pop(0)  # Tomamos el primer nodo y su ruta

        if nodo_actual == objetivo:
            return ruta_actual  # Retornamos la ruta encontrada
        else:
            visitados.add(nodo_actual)  # Marcamos el nodo como visitado
            # Ordenamos los vecinos según la heurística (más cercano al objetivo primero)
            vecinos_ordenados = sorted(grafo[nodo_actual], key=heuristica)
            for vecino in vecinos_ordenados:
                if vecino not in visitados:
                    frontera.append((vecino, ruta_actual + [vecino]))  # Agregamos vecino y ruta actualizada

    return None  # No se encontró el objetivo

# Ejemplo de uso
inicio = 'Mi Casa'
objetivo = 'Kanna'
ruta_encontrada = greedy_best_first_search(grafo, inicio, objetivo)
if ruta_encontrada:
    print(f"Se encontro un camino desde {inicio} hasta {objetivo}: {' -> '.join(ruta_encontrada)}.")
else:
    print(f"No se encontro un camino desde {inicio} hasta {objetivo}.")
