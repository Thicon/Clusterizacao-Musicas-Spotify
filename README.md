# Projeto de Clusterização de músicas

## Descrição do projeto

Este projeto utiliza um conjunto de dados do Spotify, disponibilizada do Kaggle, que possui registros de diversas músicas. Essa base contém dados referentes a características das músicas, como: nível de instrumentalidade, dançabilidade, valência musical, e outros.

Há alguns cenários a se explorar diante a esses dados disponíveis, como: detecção de padrões das variáveis agrupadas por grupos específicos, agrupamento das músicas de acordo com diferentes fatores, análises temporais dos dados disponíveis e criações de hipóteses.

A Clustericação/agrupamento podem ser muito úteis em casos como esses, aonde não há uma variável "target" disponível, fator que é muito explorado em segmentação de clientes, à fim de realizar promoções específicas para diferentes grupos que possuem interesses e preferências diferentes. 

Linguagens, ferramentas, métodos e fatores utilizados:
- Linguagem Python
- Bibliotecas: Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, WordCloud, Joblib
- Ambiente VSCode
- Utilização de arquivos .ipynb e .py
- Versionamento de código com Git

------------------

## Etapas do projeto

O repositório inclui quatro notebooks, onde são feitas diferentes etapas do projeto.

### **01_EDA_pt1**

Nessa etapa realizei uma série de tratamentos na base de músicas entitulada como "data.csv", realizando etapas como:

  - Análise de colunas
  - Exclusão de registros duplicados
  - Tratamento de valores de colunas
  - Exibição de gráficos das distribuições das colunas

<img src="images/01_01_EDA_distribuicoes_colunas.png" alt="distribuicoes" width="700"/>

  - Analisando fatotes como a popularidade das músicas em busca de possíveis padrões nos dados

<img src="images/01_04_EDA_boxplot_popularidade_2.png" alt="popularidade" width="700"/>
    
- Análises mais aprofundadas nas variáveis


<img src="images/01_09_EDA_analise_variaveis_valencia.png" alt="valencia" width="700"/>

Podemos ver acima por exemplo, que há uma correlação positiva entre valência musical e acusticidade.

------------------

### **01_EDA_pt2**

Nesse notebook realizei alguns tratamentos nas variáveis númericas, incluindo a criação de intervalos para variáveis numéricas.

- Isso com o objetivo de analisar as palavras presentes no nome das das músicas, baseado em um intervalo de valores da coluna, por exemplo, as palavras mais frequêntes quando o nível de instrumentalidade é de 0-0,25 e 0,75-1.
- Obs: Para ajudar na visualização, optei por ocultar algumas palavras que se repetiam muito no nome das músicas, como as conhecidas "wordstops".

<img src="images/01_15_EDA_instrumentalidade.png" alt="instrumentalidade" width="700"/>

Ao analisarmos essas nuvens, podemos ver a influência do nivel de intrumentalidade nos nomes.

- Agora, a coluna "Energia":

<img src="images/01_16_EDA_energia.png" alt="energia" width="700"/>

Ao analisarmos as nuvens de "Energia", conseguimos encontrar algumas curiosidades, como: em músicas com níveis mais baixos de energia, palavras como: concerto, flat major e sonata, aparecem com maior frequência do que nas músicas com níveis mais altos.

------------------

### **02_Clusterização**

Nesse notebook fiz a criação de um modelo KMeans utilizando variáveis numéricas contínuas. Aproveitei para:

  - Analisar o uso do PCA em algumas colunas de alta multicolinearidade

<img src="images/02_01_Clusterizacao_variancia_explicada_pca.png" alt="pca" width="400"/>

  - Detecção do número de k(grupos) do KMeans com o Elbow Method - Método do Cotovelo
  - 
Obs: Há outras maneiras de se analisar isso, uma delas é o "silhouette_score".

<img src="images/02_03_Clusterizacao_grafico_cotovelo.png" alt="pca" width="400"/>

  - Análise das variáveis, através de gráficos de disperção

As cores variam de acordo com o Cluster

<img src="images/02_04_Clusterizacao_scatter_5.png" alt="scatter5" width="700"/>

<img src="images/02_04_Clusterizacao_scatter_8.png" alt="scatter8" width="700"/>
  
  - Visualizações dos quartis e distribuições das colunas, de acordo com os clusters

<img src="images/02_05_Clusterizacao_box_colunas.png" alt="box_col" width="700"/>

Podemos ver que alguns clusters herdaram características específicas de determinadas colunas, como niveis altos em uma, baixos em outras...

  - Visualização das palavras mais frequentes nos nomes das músicas, baseado nos clusters

<img src="images/02_06_Clusterizacao_nuvem_clusters.png" alt="nuvens_clusters" width="700"/>
    
Análises detalhadas das colunas, com insights plotados

- Energia
<img src="images/02_07_Clusterizacao_box_energy.png" alt="box_energy" width="800"/>

- Acusticidade
<img src="images/02_07_Clusterizacao_box_acousticness.png" alt="box_acousticness" width="800"/>

- Valência musical
<img src="images/02_07_Clusterizacao_box_valence.png" alt="box_valence" width="800"/>


- A descrição das características dos clusters está presente no notebook 02_Clusterizacao.ipynb
- Este notebook, contém outros insights também

------------------

### **02_Clusterização_pipeline**

Criação de pipeline com pré-processamento e modelo, incluindo:
  - Seleção das features
  - Normalização dos dados - Escala 0-1
  - Criação do PCA
  - Modelo Kmeans de 5 clusters

Por fim, fiz visualizações nas bases de treinamento e teste.

------------------

### **Script Python: 03_simulando_producao**

Importação do pipeline, e aplicação em cima de um conjunto de dados separado anteriomente. Além de algumas visualizações em cima desses dados.


