import pandas as pd

data = pd.read_json('enem_2023.json')

# 1 - qual das disciplinas tem a maior amplitude de nota?

amplitude = data.max() - data.min()
print("Amplitude:\n", amplitude)
maior_amplitude = amplitude.idxmax()
print("Disciplina com maior amplitude:", maior_amplitude)


# 2 - qual é a média e a mediana para cada uma das disciplinas? (Lembre-se de remover todos os valores nulos quando considerar a mediana)
'''media = data.mean()
mediana = data.median(skipna=True)
print("Média:\n", media)
print("Mediana:\n", mediana)'''


# 3 - considerando o curso de Ciência da Computação da UFPE, onde o peso de cada uma das disciplinas é ponderado:
# a. Redação - 2 
# b. Matemática e suas Tecnologias - 4 
# c. Linguagens, Códigos e suas Tecnologias - 2 
# d. Ciências Humanas e suas Tecnologias - 1 
# e. Ciências da Natureza e suas Tecnologias - 1

# Definir os pesos
# pesos = {'Redação': 2, 'Matemática': 4, 'Linguagens': 2, 'Ciências humanas': 1, 'Ciências da natureza': 1}

# calcular a nota ponderada
'''data['Nota Ponderada'] = (data['Redação'] * pesos['Redação'] +
                          data['Matemática'] * pesos['Matemática'] +
                          data['Linguagens'] * pesos['Linguagens'] +
                          data['Ciências humanas'] * pesos['Ciências humanas'] +
                          data['Ciências da natureza'] * pesos['Ciências da natureza']) / sum(pesos.values())'''

# ordenar pela nota ponderada e pegar os 500 melhores colocados
# top_500 = data.nlargest(500, 'Nota Ponderada')

# calcular média e desvio padrão
'''media_top_500 = top_500['Nota Ponderada'].mean()
desvio_padrao_top_500 = top_500['Nota Ponderada'].std()
print("Média (top 500):", media_top_500)
print("Desvio padrão (top 500):", desvio_padrao_top_500)'''


# 4 - se todos esses estudantes aplicassem para ciência da computação e existissem apenas 40 vagas, qual seria a variância e média da nota dos estudantes que entraram no curso de ciência da computação?

# pegar os 40 melhores colocados
# top_40 = top_500.nlargest(40, 'Nota Ponderada')

# calcular média e variância
'''media_top_40 = top_40['Nota Ponderada'].mean()
variancia_top_40 = top_40['Nota Ponderada'].var()
print("Média (top 40):", media_top_40)
print("Variância (top 40):", variancia_top_40)'''


# 5 - qual o valor do teto do terceiro quartil para as disciplinas de matemática e linguagens?

# Calcular o terceiro quartil
'''q3_matematica = data['Matemática'].quantile(0.75)
q3_linguagens = data['Linguagens'].quantile(0.75)
print("Teto do terceiro quartil - Matemática:", q3_matematica)
print("Teto do terceiro quartil - Linguagens:", q3_linguagens)'''


# 6 - faça o histograma de Redação e Linguagens, de 20 em 20 pontos. 
# podemos dizer que são histogramas simétricos, justifique e classifique se não assimétricas?

# import matplotlib.pyplot as plt

# Criar histogramas
'''plt.hist(data['Redação'].dropna(), bins=range(0, 1000, 20), alpha=0.5, label='Redação')
plt.hist(data['Linguagens'].dropna(), bins=range(0, 1000, 20), alpha=0.5, label='Linguagens')
plt.legend(loc='upper right')
plt.show()'''


# para determinar a simetria:

'''redacao_hist = data['Redação'].dropna().value_counts(bins=range(0, 1000, 20)).sort_index()
linguagens_hist = data['Linguagens'].dropna().value_counts(bins=range(0, 1000, 20)).sort_index()'''

# Verificar a simetria
'''redacao_simetrica = redacao_hist.skew() == 0
linguagens_simetrica = linguagens_hist.skew() == 0

print("Redação simétrica?", redacao_simetrica)
print("Linguagens simétrica?", linguagens_simetrica)'''


# 7 - agora coloque um range fixo de 0 até 1000, você ainda tem a mesma opinião quanto a simetria?

# criar histogramas com range fixo
'''plt.hist(data['Redação'].dropna(), bins=range(0, 1000, 20), range=(0, 1000), alpha=0.5, label='Redação')
plt.hist(data['Linguagens'].dropna(), bins=range(0, 1000, 20), range=(0, 1000), alpha=0.5, label='Linguagens')
plt.legend(loc='upper right')
plt.show()'''


# 8 - faça um boxplot para as notas de Ciências da Natureza e Redação, analisando os quartis e identificando possíveis outliers. 
# utilize o método IQR (Intervalo Interquartílico) para essa análise

# Criar boxplot
'''plt.boxplot([data['Ciências da natureza'].dropna(), data['Redação'].dropna()], labels=['Ciências da Natureza', 'Redação'])
plt.show()'''

# Calcular o IQR e identificar outliers
'''q1_cn = data['Ciências da natureza'].quantile(0.25)
q3_cn = data['Ciências da natureza'].quantile(0.75)
iqr_cn = q3_cn - q1_cn

q1_red = data['Redação'].quantile(0.25)
q3_red = data['Redação'].quantile(0.75)
iqr_red = q3_red - q1_red

outliers_cn = data[(data['Ciências da natureza'] < (q1_cn - 1.5 * iqr_cn)) | (data['Ciências da natureza'] > (q3_cn + 1.5 * iqr_cn))]
outliers_red = data[(data['Redação'] < (q1_red - 1.5 * iqr_red)) | (data['Redação'] > (q3_red + 1.5 * iqr_red))]

print("Outliers - Ciências da Natureza:\n", outliers_cn)
print("Outliers - Redação:\n", outliers_red)'''


# 9 - remova todos os outliers e verifique se eles são passíveis de alterar a média nacional significativamente (considere significativamente um valor acima de 5%)

# Remover os outliers
# data_sem_outliers = data[~data.index.isin(outliers_cn.index) & ~data.index.isin(outliers_red.index)]

# Calcular a média nacional sem os outliers
# media_sem_outliers = data_sem_outliers.mean()

# Verificar se a média foi alterada significativamente
'''alteracao_significativa = (media - media_sem_outliers).abs() / media > 0.05
print("Alteração significativa nas médias:\n", alteracao_significativa)'''


# 10 - considerando valores nulos, tente encontrar qual seria a melhor medida de tendência que pode substituir as notas nulas. 
# média, moda ou mediana? substitua o valor por todos os três e diga qual delas altera menos a média geral e o desvio padrão

# Substituir valores nulos por média, moda e mediana
'''data_media = data.fillna(data.mean())
data_moda = data.apply(lambda x: x.fillna(x.mode()[0]), axis=0)
data_mediana = data.fillna(data.median(skipna=True))'''

# Calcular a média e desvio padrão para cada substituição
'''media_media = data_media.mean()
desvio_media = data_media.std()
media_moda = data_moda.mean()
desvio_moda = data_moda.std()
media_mediana = data_mediana.mean()
desvio_mediana = data_mediana.std()'''

# Comparar com a média e desvio padrão originais
'''alteracao_media = (media - media_media).abs() / media, (media - media_moda).abs() / media, (media - media_mediana).abs() / media
alteracao_desvio = (data.std() - desvio_media).abs() / data.std(), (data.std() - desvio_moda).abs() / data.std(), (data.std() - desvio_mediana).abs() / data.std()

print("Alteração média (média, moda, mediana):\n", alteracao)'''