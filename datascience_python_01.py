# -*- coding: utf-8 -*-
"""
Funcional e OO
Aula 4
Data Science com Pandas
Neylson Crepalde
"""

import pandas as pd

pnad = pd.read_csv("https://raw.githubusercontent.com/neylsoncrepalde/introducao_ao_python/master/pes_2012.csv")

pnad.shape
pnad.columns

pnad.head()

pnad["V8005"].dtype
pnad["V0302"]
pnad["V4720"]

# Estudando a idade 
pnad["V8005"].describe().round(decimals = 2)

m = pnad["V8005"].mean()
round(m, 2)

pnad["V8005"].var()

pnad["V0302"].value_counts()

tab_sexo = pd.crosstab(index = pnad["V0302"],
            columns = ["contagem"])

print("Distribuição da Frequência - Sexo" + "\n")
print(tab_sexo)

print("Porcentagens - Sexo" + "\n")
print((tab_sexo / tab_sexo.sum()) * 100)

# Estudando a variável cor/raça
tab_cor = pnad["V0404"].value_counts()

print("Distribuição de Frequências - Cor" + "\n")
print(tab_cor)

print("Porcentagens - Cor" + "\n")
print( (tab_cor / tab_cor.sum())*100 )

# Cruzando sexo e cor
sexo_cor = pd.crosstab(index = pnad["V0404"],
                       columns = pnad["V0302"])
print(sexo_cor)

### Estudando a renda
pnad.columns
pnad["V4720"].astype(float)






