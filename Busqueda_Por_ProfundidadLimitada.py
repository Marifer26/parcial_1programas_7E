def busq_prof_lim(grafo, inicio, objetivo, limite_profundidad):
    
    visitados = set()     # Conjunto para llevar un seguimiento de los nodos visitados
    stack = [(inicio, [inicio], 0)]     # Pila para realizar la búsqueda en profundidad

    while stack:
        
        nodo, camino, profundidad = stack.pop()  # Extraer el nodo actual, su camino y su profundidad desde la pila
        if profundidad > limite_profundidad:
            continue  # Si se excede el límite de profundidad, pasa al siguiente nodo
        
        if nodo not in visitados:
            visitados.add(nodo)  # Marcar el nodo como visitado en caso de que no haya sido visitado

            if nodo == objetivo: 
                return camino  # Devolver el camino si se encuentra el nodo objetivo
            
            # Extender la pila con los vecinos del nodo actual
            for vecino in grafo[nodo]:
                stack.append((vecino, camino + [vecino], profundidad + 1))

    # Si no se encuentra un camino dentro del límite de profundidad, devolver un mensaje
    return "No se encontro un camino dentro del limite de profundidad."

# Grafo con los nuevos nombres de los nodos
grafo = {
    'Trabajo': ['La Perla', 'OXXO'],
    'La Perla': ['Trabajo', 'Terraza Oblatos', 'Salon'],
    'OXXO': ['Trabajo', 'Entrada de la Escuela'],
    'Terraza Oblatos': ['La Perla'],
    'Salon': ['La Perla', 'Entrada de la Escuela'],
    'Entrada de la Escuela': ['OXXO', 'Salon', 'CUCS'],
    'CUCS': ['Transito', 'Centro Historico'],
    'Transito': ['CUCS', 'Plaza Galerias'],
    'Centro Historico': ['CUCS', 'Plaza Andares'],
    'Plaza Galerias': ['Transito'],
    'Plaza Andares': ['Centro Historico']
}

inicio = 'Trabajo'
objetivo = 'Salon'
limite_profundidad = 3

print("Camino recorrido para llegar al salon desde mi trabajo:", busq_prof_lim(grafo, inicio, objetivo, limite_profundidad))
