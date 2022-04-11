import numpy as np

def matriz_confusao(esperados, estimados):
    tp, fp, tn, fn = 0, 0, 0, 0
    for par in zip(esperados, estimados):
        if par[0] and par[1]:
            tp += 1
        elif par[0] and not par[1]:
            fn += 1
        elif not par[0] and not par[1]:
            tn += 1
        elif not par[0] and par[1]:
            fp += 1
    return np.array([tp, fp, tn, fn])