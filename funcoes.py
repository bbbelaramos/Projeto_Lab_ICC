#importando pandas, scipy, matplotlib e o dataset de câncer de mama do sklearn
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

COLUNAS_DESEJADAS = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness','mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension']

#funções carregamento, limpeza e análise descritiva dos dados
def carregar_dados():
    dados_brutos = load_breast_cancer()
    #fazendo uma tabela com todas as 30 colunas
    tabela = pd.DataFrame(dados_brutos.data, columns=dados_brutos.feature_names)

    #.copy() para garantir que é uma tabela independente
    tabela_nova = tabela[COLUNAS_DESEJADAS].copy()
    #adicionando a coluna de target(diagnostico)
    tabela_nova['diagnostico'] = dados_brutos.target 

    return tabela_nova
def limpar_dados():
    tabela = carregar_dados()
    
    #tabela com a contagem de valores nulos por coluna
    tabela_nula = tabela.isna().sum() 
    #remove as linhas com valores nulos, caso haja algum. 
    #remove a linha se pelo menos um valor estiver nulo
    if tabela_nula.sum() > 0:
        tabela = tabela.dropna()

    #tabela com a quantidade de valores duplicados
    tabela_duplicada = tabela.duplicated().sum() 
    #remove as linhas duplicadas, caso haja algum
    if tabela_duplicada > 0:
        tabela = tabela.drop_duplicates()


    print(f'Valores nulos por coluna:\n{tabela_nula}')
    print(f'Valores duplicados: {tabela_duplicada}')

    return tabela
def analisar_descritiva_geral(tabela):

    #cálculo de estatísticas descritivas para cada coluna da tabela
    tabela_descritiva = tabela.describe()
    return tabela_descritiva
def analisar_descritiva_por_grupo(tabela):

    tabela_benig_malig = tabela.groupby('diagnostico').mean()
    return tabela_benig_malig


#funções para testar a diferença entre os grupos, calcular correlação e identificar outliers
def testar_diferenca_grupos(tabela):

    grupo_maligno = tabela[tabela['diagnostico'] == 0]
    grupo_benigno = tabela[tabela['diagnostico'] == 1]

    #cria um dicionário para armazenar os resultados dos testes de Mann-Whitney U
    resultados = {}
    for coluna in COLUNAS_DESEJADAS:
        estatistica, p_valor = stats.mannwhitneyu(grupo_maligno[coluna], grupo_benigno[coluna])
        resultados[coluna] = p_valor
        print(p_valor)

    return resultados
def calcular_correlacao(tabela):

    correlacao = tabela.corr()
    print
    return correlacao
def identificar_outliers(tabela):

    outliers = {}
    for coluna in COLUNAS_DESEJADAS:
        Q1 = tabela[coluna].quantile(0.25)
        Q3 = tabela[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        outliers[coluna] = tabela[(tabela[coluna] < limite_inferior) | (tabela[coluna] > limite_superior)]


        if len(outliers[coluna]) > 0:
            contagem = outliers[coluna]['diagnostico'].value_counts()
            print(f'Outliers na coluna {coluna}:')
            print(contagem)

    return outliers



def plotar_histograma(tabela,coluna):
    tabela[coluna].hist()
    plt.title(f'Histograma de {coluna}')
    plt.show()
def plotar_todos_histogramas(tabela):
    for coluna in COLUNAS_DESEJADAS:
        plotar_histograma(tabela, coluna)

plotar_todos_histogramas(carregar_dados())