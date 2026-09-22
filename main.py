#importando as funcoes do arquivo funcoes.py
import funcoes as f

dados = f.limpar_dados()

print(f.analisar_descritiva_geral(dados))
print(f.analisar_descritiva_por_grupo(dados))
print(f.testar_diferenca_grupos(dados))
print(f.calcular_correlacao(dados))
print(f.identificar_outliers(dados))