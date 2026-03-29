# 🎵 Análise de Dados do Spotify: Pipeline ETL com Python e Pandas

## Sobre o Projeto
Este projeto consiste em um pipeline de dados (Extração, Transformação e Carga - ETL) desenvolvido em Python. O objetivo principal é extrair insights sobre o perfil sonoro de artistas específicos (neste estudo de caso, focado no repertório pop) a partir de uma base de dados bruta de músicas do Spotify. 

O script processa grandes volumes de dados, realiza a limpeza e higienização das informações e exporta um arquivo estruturado, pronto para ser consumido por ferramentas de Business Intelligence (BI).

##  Tecnologias e Bibliotecas Utilizadas
* **Python 3:** Linguagem principal do projeto.
* **Pandas:** Utilizado para manipulação, filtragem e agregação de dados em DataFrames.
* **Git/GitHub:** Versionamento de código e documentação.

##  Arquitetura do Pipeline (ETL)
O projeto segue uma estrutura clássica de processamento de dados:

1. **Extração (Extract):** Leitura de um dataset massivo (`.csv`) contendo milhares de registros de músicas do Spotify.
2. **Transformação (Transform):** * Filtragem de registros focados em um alvo específico.
   * Seleção de colunas relevantes para a regra de negócio (Popularidade, Dançabilidade, Energia, Valência e Acústica).
   * Higienização de dados: Identificação e remoção de registros duplicados (tratamento de versões ao vivo, remixes, etc.).
   * Cálculo de métricas agregadas (médias de energia e positividade sonoras).
3. **Carga (Load):** Exportação dos dados limpos e transformados para um novo arquivo estruturado (`dados_limpos_sabrina_carpenter.csv`), otimizado para a criação de dashboards.

##  Principais Insights Gerados
O algoritmo realiza uma análise exploratória automática que responde a perguntas de negócio como:
* Quais são as faixas mais populares do artista no momento?
* Qual é a média de "Energia" (intensidade e velocidade) da discografia?
* Qual faixa possui o maior índice de "Dançabilidade" (potencial para pistas de dança)?

##  Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/analise-dados-spotify.git](https://github.com/SEU-USUARIO/analise-dados-spotify.git)

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Instale as dependências
   ```bash
   pip install pandas

6. Baixe um dataset de faixas do Spotify via Kaggle, renomeie para dataset_spotify.csv e coloque na raiz do projeto.

7. Execute o script de análise:
   ```bash
   python analise_sabrina.py
