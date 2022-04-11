
##Tratamento dos dados
##Mapear as idades em faixas etárias

import numpy as np

def faixa_etaria(idade):
    if idade == np.nan:
        return 'NaoConhecida'
    elif 0.0 <= idade <= 10.0:
        return 'Criança'
    elif 11.0 <= idade <= 18.0:
        return 'Jovem'
    elif 19.0 <= idade <= 50.0:
        return 'Adulto'
    else:
        return 'Idoso'