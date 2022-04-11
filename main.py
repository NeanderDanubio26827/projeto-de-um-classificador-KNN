
import pandas as pd
import numpy as np
from matplotlib.pyplot import plot
from collections import Counter
from matriz_confusao import matriz_confusao
from acuracia import acuracia
from faixa_etaria import faixa_etaria
from distancia_hamming import distancia_hamming
from mais_frequente import mais_frequente

# y (sobreviveu) é minha variável alvo
# x (Classe, idade, sexo) é minha variável atributo descritivo
# Trata-se de um problema de classificação

# importação da base de dados
df = pd.read_csv('https://query.data.world/s/c2ixg24yogu6pgudqodbhn5ynrvdjr')
df.head() #exibe a base de dados
print(df.head())
#print(faixa_etaria(12.0)) # testa a função faixa_etária

 #mapeia as idades em faixas etárias
 #utilizando list compreenhsion 
 #cria um novo atributo na base de dados
 #chamado "faixa_etaria"
 #Que pode ter os valores: Criança, Jovem, Adulto e Idoso
 
df['FaixaEtaria']= [faixa_etaria(k) for k in df['Idade'].values]
df = df[['Classe','Sexo','FaixaEtaria','Sobreviveu']]
df.head()

#separação da base de dados 
#em um conjunto de treino
#usados para treinar o algoritmo
treino = df.iloc[:int(len(df.index)*0.7)]

#Separação da base de dados 
#Em um cojunto de teste
#Dados que serão utilizados
#Para verificar a eficiência
#do KNN
teste = df.iloc[int(len(df.index)*0.7)+1:]

print(df)
print(treino.index)
print(teste.index)

print(df.iloc[1])
print(df.iloc[2])
print('\nDistânica:', distancia_hamming(df.iloc[1],df.iloc[2]))