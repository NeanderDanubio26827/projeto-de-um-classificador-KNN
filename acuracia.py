from matriz_confusao import matriz_confusao
import numpy as np

def acuracia(esperados, estimados):
    #n = len(esperados)
    tp, fp, tn, fn = matriz_confusao(esperados, estimados)
    return ((tp+tn)/(tp+fp+tn+fn))

print(acuracia([1,1,0,0],[0,0,0,0]))