# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioIA - Sistema Inteligente de Apoio à Triagem de Risco Cardiovascular

## 👨‍🎓 Integrantes

- Henrique Honorio da Silva – RM 567102
- João Victor Matos de Paiva – RM 568345
- Luiz Frederico Nunes Campêlo – RM 567319
- Manoella Menezes Weiser – RM 567531
- Mariana Carvalho Youn – RM 568548

## 👩‍🏫 Professores

### Tutor(a)

- Leonardo Ruiz Orabona

### Coordenador(a)

- André Godoi Chiovato

## 📜 Descrição

O CardioIA é um projeto desenvolvido com o objetivo de aplicar técnicas de Inteligência Artificial e Processamento de Linguagem Natural em um cenário de apoio à triagem de risco cardiovascular.

Nesta fase do projeto, foram desenvolvidas duas partes principais.

A **Parte 1** consiste na criação de um mapa de conhecimento capaz de relacionar pares de sintomas a possíveis condições associadas. O sistema realiza a leitura de um arquivo CSV contendo essas relações e identifica, em frases fornecidas pelo usuário, quais sintomas estão presentes. Quando os sintomas encontrados correspondem a um par existente no mapa de conhecimento, o sistema apresenta a possível condição associada.

A **Parte 2** consiste no desenvolvimento de um classificador de risco utilizando aprendizado de máquina. Para isso, foi criado um dataset contendo frases classificadas em duas categorias: **alto risco** e **baixo risco**.

As frases do dataset são transformadas em características numéricas utilizando a técnica **TF-IDF (Term Frequency-Inverse Document Frequency)**. Em seguida, essas características são utilizadas para treinar um modelo de **Regressão Logística**, responsável por classificar novas frases de acordo com as categorias presentes no dataset.

O modelo foi avaliado utilizando dados de treinamento e teste, além de métricas como acurácia, precisão, recall e F1-score. Também foram realizados testes com novas frases para verificar o comportamento do classificador.

O projeto possui finalidade acadêmica e experimental. As classificações realizadas pelo sistema não representam diagnóstico médico e não substituem avaliação ou orientação de profissionais de saúde.

## 📁 Estrutura de arquivos

Os principais arquivos desenvolvidos nesta fase são:

- **mapa_conhecimento.csv**: contém os pares de sintomas e as respectivas condições associadas utilizadas pelo mapa de conhecimento.

- **frases_sintomas.txt**: contém as frases utilizadas nos testes de identificação de sintomas.

- **extracao_sintomas.py**: realiza a leitura do mapa de conhecimento, identifica os sintomas presentes nas frases e verifica as associações existentes.

- **dataset_risco.csv**: contém as frases utilizadas para o treinamento e teste do classificador de risco, divididas entre as categorias "alto risco" e "baixo risco".

- **verificar_dataset.py**: realiza a leitura do dataset de risco e apresenta sua estrutura e a quantidade de exemplos existentes em cada situação.

- **classificador_risco.py**: realiza o treinamento, avaliação e teste do classificador utilizando TF-IDF e Regressão Logística.

- **README.md**: documentação do projeto e instruções para execução dos códigos.

## 🔧 Como executar o código

### Pré-requisitos

Para executar o projeto, é necessário possuir:

- Python 3.13;
- Visual Studio Code ou outra IDE compatível com Python;
- acesso ao terminal;
- bibliotecas `pandas` e `scikit-learn`.

As versões utilizadas durante o desenvolvimento foram:

- Python 3.13.7
- pandas 2.3.3
- scikit-learn 1.8.0
- scipy 1.17.1

### Instalação das bibliotecas

No terminal, dentro da pasta do projeto, execute:

    pip install pandas scikit-learn

Para verificar as versões instaladas:

    python --version
    pip show pandas
    pip show scikit-learn
    pip show scipy

---

## 🧠 Parte 1 - Mapa de Conhecimento

A Parte 1 utiliza o arquivo `mapa_conhecimento.csv`, que contém as relações entre pares de sintomas e possíveis condições associadas.

O arquivo `frases_sintomas.txt` contém as frases utilizadas para testar a identificação dos sintomas.

### Execução

No terminal, dentro da pasta do projeto, execute:

    python extracao_sintomas.py

O programa apresenta o mapa de conhecimento, identifica os sintomas presentes em cada frase e verifica se existe uma associação correspondente no mapa.

### Exemplo de resultado

    Frase: Há dois dias estou sentindo uma dor forte no peito que piora quando faço esforço físico e está dificultando minhas atividades diárias.

    Sintomas encontrados: ['dor forte no peito', 'esforço físico']

    Possível condição associada: Infarto

Outro exemplo:

    Frase: Desde ontem sinto um aperto no tórax acompanhado de falta de ar depois de realizar esforço físico, e preciso parar a atividade para que o desconforto diminua.

    Sintomas encontrados: ['falta de ar', 'aperto no tórax', 'esforço físico']

    Possível condição associada: Angina

---

## 🤖 Parte 2 - Classificador de Risco

A Parte 2 utiliza o arquivo `dataset_risco.csv`, contendo exemplos classificados como **alto risco** ou **baixo risco**.

### Verificação do dataset

Antes de executar o classificador, é possível verificar o conteúdo do dataset utilizando:

    python verificar_dataset.py

O programa apresenta os exemplos existentes e a quantidade de frases em cada situação.

O dataset utilizado nesta fase possui:

- 20 frases no total;
- 10 exemplos classificados como "alto risco";
- 10 exemplos classificados como "baixo risco".

### Execução do classificador

Para executar o classificador:

    python classificador_risco.py

O programa realiza as seguintes etapas:

1. Leitura do dataset;
2. Separação das frases e respectivas classificações;
3. Divisão dos dados em conjuntos de treinamento e teste;
4. Transformação dos textos em características numéricas utilizando TF-IDF;
5. Criação do modelo de Regressão Logística;
6. Treinamento do modelo;
7. Realização das previsões;
8. Avaliação do desempenho do modelo;
9. Comparação entre classificações reais e previstas;
10. Teste do modelo com novas frases.

---

## 📊 Resultados obtidos

Durante os testes realizados com o dataset, foram utilizados:

- **20 frases** no total;
- **10 exemplos de alto risco**;
- **10 exemplos de baixo risco**;
- **14 frases para treinamento**;
- **6 frases para teste**;
- **62 características geradas pelo TF-IDF**.

O modelo apresentou a seguinte acurácia:

    ACURÁCIA DO MODELO: 0.8333333333333334
    ACURÁCIA EM PORCENTAGEM: 83.33%

### Relatório de classificação

    precision    recall  f1-score   support

    alto risco       1.00      0.67      0.80         3
    baixo risco      0.75      1.00      0.86         3

    accuracy                           0.83         6
    macro avg         0.88      0.83      0.83         6
    weighted avg      0.88      0.83      0.83         6

### Comparação entre valor real e previsão

No conjunto de teste, o modelo apresentou:

- 5 classificações corretas;
- 1 classificação incorreta;
- 6 exemplos utilizados no conjunto de teste;
- acurácia de 83,33%.

A classificação incorreta ocorreu para a frase:

    meu coração está batendo muito rápido e tenho palpitações

Classificação real:

    alto risco

Classificação prevista:

    baixo risco

As demais cinco frases do conjunto de teste foram classificadas corretamente.

### Análise do resultado

A acurácia de 83,33% ocorreu porque uma das seis frases do conjunto de teste foi classificada incorretamente. A frase "meu coração está batendo muito rápido e tenho palpitações" pertencia à categoria "alto risco", mas o modelo a classificou como "baixo risco".

Esse resultado indica que o modelo conseguiu identificar corretamente a maioria dos padrões presentes no conjunto de teste, mas apresentou dificuldade em reconhecer esse exemplo específico. Como o dataset utilizado nesta fase possui apenas 20 frases, sendo 14 destinadas ao treinamento e 6 ao teste, cada erro possui um impacto significativo na acurácia final.

Portanto, o resultado de 83,33% não significa que o modelo esteja 83,33% correto em situações médicas reais. Ele representa o desempenho obtido especificamente sobre o pequeno conjunto de teste utilizado nesta fase do projeto. A ampliação do dataset e a inclusão de mais exemplos variados podem contribuir para uma avaliação mais robusta do modelo em fases futuras.

---

## 🧪 Testes com novas frases

Após o treinamento, o modelo também foi testado com novas frases.

### Teste 1

    Frase: estou sentindo uma dor forte no peito e falta de ar
    Classificação: alto risco

### Teste 2

    Frase: tenho um pequeno desconforto nas costas
    Classificação: baixo risco

### Teste 3

    Frase: sinto pressão no peito acompanhada de suor frio
    Classificação: alto risco

### Teste 4

    Frase: estou um pouco cansado depois de estudar
    Classificação: baixo risco

Os resultados demonstraram que o modelo conseguiu classificar corretamente essas quatro novas frases de acordo com as categorias definidas no dataset.

## ⚠️ Observação

O sistema desenvolvido possui finalidade acadêmica e experimental.

As classificações de risco apresentadas pelo modelo não constituem diagnóstico médico e não devem ser utilizadas como substituição de avaliação, diagnóstico ou orientação de profissionais de saúde.

---

## 🗃 Histórico de lançamentos

- **0.2.0 - 03/10/2026**
  - Implementação do classificador de risco cardiovascular.
  - Criação do dataset de risco com exemplos de alto e baixo risco.
  - Aplicação de TF-IDF para representação dos textos.
  - Implementação do modelo de Regressão Logística.
  - Avaliação do modelo utilizando acurácia e relatório de classificação.
  - Comparação entre classificações reais e previstas.
  - Testes do modelo com novas frases.

- **0.1.0 - 03/10/2026**
  - Criação do mapa de conhecimento.
  - Desenvolvimento da identificação de sintomas em frases.
  - Associação entre pares de sintomas e possíveis condições.
  - Criação dos arquivos utilizados nos testes.

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">

<a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">CardioIA - Sistema Inteligente de Apoio à Triagem de Risco Cardiovascular</a>

por

<a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a>

está licenciado sobre

<a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.

</p>