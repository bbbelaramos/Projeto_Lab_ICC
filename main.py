#importando as funcoes do arquivo funcoes.py
from funcoes import carregar_dados, limpar_dados, analisar_descritiva_geral, analisar_descritiva_por_grupo, testar_diferenca_grupos, calcular_correlacao, identificar_outliers

dados = limpar_dados()

print(analisar_descritiva_geral(dados))
print(analisar_descritiva_por_grupo(dados))
print(testar_diferenca_grupos(dados))
print(calcular_correlacao(dados))
print(identificar_outliers(dados))