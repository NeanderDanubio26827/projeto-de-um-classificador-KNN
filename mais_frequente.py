from collections import Counter

def mais_frequente(array):
    frequencias = Counter(array)
    return max(frequencias, key=frequencias.get)