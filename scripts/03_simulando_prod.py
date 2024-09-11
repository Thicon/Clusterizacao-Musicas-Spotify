# %% 
# 1. Importando bibliotecas

import joblib
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# %%
# 2. Importando os dados para testes
testes = pd.read_csv("../data/dados_testes.csv")

# %% 
# 3. Importando o pipeline
pipeline = joblib.load('../models/pipeline.joblib')

# %%
# 4. Realizando o predict:
pipeline.predict(testes)

# %% 
# 5. Analisando os clusters
testes['Cluster'] = pipeline.predict(testes)
testes['Cluster'].value_counts()

# %% 
# 6. Visualizando as nuvens dos nomes das músicas
cluster_0 = testes.loc[testes['Cluster'] == 0, "name"].to_list()
cluster_1 = testes.loc[testes['Cluster'] == 1, "name"].to_list()
cluster_2 = testes.loc[testes['Cluster'] == 2, "name"].to_list()
cluster_3 = testes.loc[testes['Cluster'] == 3, "name"].to_list()
cluster_4 = testes.loc[testes['Cluster'] == 4, "name"].to_list()

nuvem_cluster_0_teste = ''.join(map(str, cluster_0))
nuvem_cluster_1_teste = ''.join(map(str, cluster_1))
nuvem_cluster_2_teste = ''.join(map(str, cluster_2))
nuvem_cluster_3_teste = ''.join(map(str, cluster_3))
nuvem_cluster_4_teste = ''.join(map(str, cluster_4))

fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(12,10), tight_layout=True)

lista_nuvens = [nuvem_cluster_0_teste, nuvem_cluster_1_teste, nuvem_cluster_2_teste, nuvem_cluster_3_teste, nuvem_cluster_4_teste]

titulos = ["Cluster 0", "Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4"]

palavras_ocultar = ['and','or','when','why','the','he','she','it','him','her','they','are','is','am','no','me',
                    'feat','to','a','from','for','at','with','that','feat','in','my','i','op','you','up','de',
                    'all','of','one','on','will','can','be','make','do','out','not','your','go','got','get','mi',
                    "i'm", 'el','live','remastered',"don't",'like','this','come','take','want','his','page','und','die','love','single']

for i, a, t in zip(lista_nuvens, ax.flat, titulos):
    wordcloud = WordCloud(stopwords=palavras_ocultar).generate(i)
    a.imshow(wordcloud, interpolation = 'bilinear')
    a.axis('off')
    a.set_title(t, fontsize=12)
    
plt.suptitle("Nuvem de palavras - Clusters - Treino", fontsize=16)
ax[2][1].axis('off')
plt.show()