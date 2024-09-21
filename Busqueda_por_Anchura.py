from collections import deque

def bfs(grafico, inicio, meta):
    visitado = set()  # Conjunto para almacenar los nodos visitados.
    cola = deque([[inicio]])  # Cola de caminos por verificar.

    if inicio == meta:  # Si el nodo de inicio es igual al nodo de meta.
        print("El nodo de inicio es igual al nodo de meta")
        return

    while cola:  # Mientras haya caminos por verificar.
        camino = cola.popleft()  # Obtenemos el primer camino de la cola.
        vertice = camino[-1]  # El último nodo del camino actual.

        if vertice not in visitado:  # Si el nodo no ha sido visitado.
            vecinos = grafico[vertice]  # Obtenemos los vecinos del nodo.

            for vecino in vecinos:  # Para cada vecino.
                nuevo_camino = list(camino)  # Creamos una copia del camino actual.
                nuevo_camino.append(vecino)  # Añadimos el vecino al final del camino.
                cola.append(nuevo_camino)  # Añadimos el nuevo camino a la cola.

                if vecino == meta:  # Si el vecino es el nodo de meta.
                    print("Camino desde {} hasta {}:".format(inicio, meta))
                    print(nuevo_camino)  # Imprimimos el camino.
                    return

            visitado.add(vertice)  # Marcamos el nodo como visitado.

    print("No hay camino desde {} hasta {}".format(inicio, meta))  # Si no encontramos un camino.

# Grafo con los nuevos nombres de los nodos
grafico = {
    'Entrada': {'Cochera', 'Primera sala'},
    'Cochera': {'Entrada', 'Cuarto', 'Patio'},
    'Primera sala': {'Entrada', 'Comedor'},
    'Cuarto': {'Cochera', 'Escaleras'},
    'Patio': {'Cochera', 'Segunda sala'},
    'Comedor': {'Primera sala', 'Cocina'},
    'Escaleras': {'Cuarto'},
    'Segunda sala': {'Patio'},
    'Cocina': {'Comedor', 'Refrigerador'},
    'Refrigerador': {'Cocina'},
}

bfs(grafico, 'Entrada', 'Refrigerador')
