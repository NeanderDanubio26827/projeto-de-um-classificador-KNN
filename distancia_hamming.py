## distancia de hamming
def distancia_hamming(a, b):
    chaves = a.keys()
    
    distancia = sum(a[k] != b[k] for k in chaves)
    
    return distancia/len(chaves)