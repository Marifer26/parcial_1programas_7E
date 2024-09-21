grafo = {
    'Guadalajara': {'Ameca': 83, 'Mascota': 200, 'Compostela': 260},
    'Ameca': {'Guadalajara': 83, 'Mascota': 120, 'San Sebastian del Oeste': 160},
    'Mascota': {'Guadalajara': 200, 'Ameca': 120, 'Puerto Vallarta': 100},
    'San Sebastian del Oeste': {'Ameca': 160, 'Puerto Vallarta': 60},
    'Compostela': {'Guadalajara': 260, 'Puerto Vallarta': 180},
    'Puerto Vallarta': {'Mascota': 100, 'San Sebastian del Oeste': 60, 'Compostela': 180}
}

# Función heurística (admisible y consistente)
def heuristica(nodo_actual, nodo_destino):
    
    estimaciones = {
        ('Guadalajara', 'Puerto Vallarta'): 200,
        ('Ameca', 'Puerto Vallarta'): 160,
        ('Mascota', 'Puerto Vallarta'): 100,
        ('San Sebastian del Oeste', 'Puerto Vallarta'): 60,
        ('Compostela', 'Puerto Vallarta'): 180,
        ('Puerto Vallarta', 'Puerto Vallarta'): 0
    }
    return estimaciones.get((nodo_actual, nodo_destino), 100)

# Algoritmo AO*
def AO_estrella(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]  # Cola de nodos a explorar
    visitado = {inicio}  # Conjunto de nodos visitados

    while cola:
        (nodo, camino, costo) = cola.pop(0)

        for vecino in grafo[nodo].keys():
            if vecino == destino:
                return camino + [vecino], costo + grafo[nodo][vecino]
            else:
                if vecino not in visitado:
                    visitado.add(vecino)
                    costo_total = costo + grafo[nodo][vecino] + heuristica(vecino, destino)
                    cola.append((vecino, camino + [vecino], costo_total))

inicio = 'Guadalajara'
destino = 'Puerto Vallarta'
ruta_optima, costo_optimo = AO_estrella(grafo, inicio, destino)
print(f'Ruta optima de Guadalajara a Vallarta: {ruta_optima}')
print(f'Distancia: {costo_optimo} km')
