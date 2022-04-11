from numpy import indices


def knn (baseDados, k, x, y, funcao_distancia, funcao_mesclagem):
    distancias = { indice : funcao_distancia(x, baseDados.loc[indice]) for indice in baseDados.index}

    indices = sorted(distancias, key=distancias.get)
    
    vizinhos = baseDados.loc[indices[:k]]
    
    y_estimado = funcao_mesclagem(vizinhos[y].values)
    
    return y_estimado
    
    