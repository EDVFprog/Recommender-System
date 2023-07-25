#Importing libraries
import math
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.neighbors import NearestNeighbors

def Aval_usuario(aval_df, filme):
    """Essa função obtem as avaliações dos usuarios interando por filme e deixando os valores NAN"""
    return aval_df.loc[filme, :].dropna().index.values
def ktop(Corr_df, usuario, usuarios_aval,k_viz=5):#Recebe a matriz de correlação, o usuario, a matriz de avaliaçao dos usuarios e a definição do valor de k
    return Corr_df[usuario][usuarios_aval].nlargest(k_viz).to_dict()
def aval_sV(aval_df, usuario, filme):
    """Função que diminui a avaliação do usuario da média, eliminando vies"""
    ma = aval_df[usuario].mean()
    a = aval_df.loc[filme, usuario]
    return Vies(a, ma)
def Vies(avaliacao,med_aval ):
    """Função que subtrai o vies da escala, isto é, a avaliação do usuário-media das avaliaçoes"""
    return avaliacao - med_aval
def aval_similares(aval_df,vizinhos, filme):
    """Essa função ajusta o vies das avaliações para todos os usuarios"""
    return [aval_sV(aval_df,vizinho, filme)for vizinho in vizinhos]

def med_pond__das_avals_vizinhas(avals, dist_viz):
    """ Essa função calcula a media ponderada das avaliações vizinhas, por meio da distância entre elas"""
    som_pond = np.array(avals).dot(np.array(dist_viz))# faz o produto escalar dos arrays de avaliacao e de distancia entre os vizinhos
    dist_abs = np.abs(dist_viz)#retira a raiz quadrada
    return som_pond / np.sum(dist_abs)

def aval_us(aval_df, usuario,aval_vizinho):
    med_us= aval_df[usuario].mean()
    return round(med_us+ aval_vizinho, 2)
def previsao(df,Corr,usuario,filme,k_vizinhos=5):
    """Prever o valor da avaliação d eum usuario baseado no usuario similar a ele"""
    aval_df = df.copy()

    usuario_aval = Aval_usuario(aval_df, filme)

    dist_k_vizinhos = ktop(
        Corr, usuario, usuario_aval, k_vizinhos
    )
    vizinhos, dist = dist_k_vizinhos.keys(), dist_k_vizinhos.values()

    print(f"Top-K {k_vizinhos} vizinhos do usuário {usuario}, {filme}: {list(vizinhos)}")

    avals = aval_sV(aval_df, vizinhos, filme)
    med_aval_vizinhos = med_pond__das_avals_vizinhas(avals, list(dist))

    return aval_us(aval_df, usuario, med_aval_vizinhos)
dffinal= dfT.copy()
for usuario, filmes in  dffinal.iteritems():
    for filme in filmes.keys():
        if np.isnan(dffinal.loc[filme, usuario]):
           dffinal.loc[filme, usuario] = previsao(dffinal, df3corr, usuario, filme)
