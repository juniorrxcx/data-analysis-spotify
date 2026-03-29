import pandas as pd

print("Iniciando a esteira de processamento de dados...")
print("Carregando o arquivo dataset_spotify.csv (isso pode levar alguns segundos)...\n")

try:
    df = pd.read_csv('dataset_spotify.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'dataset_spotify.csv' não encontrado na pasta.")
    exit()


coluna_artista = 'artists'      
coluna_musica = 'track_name'    
artista_alvo = 'Sabrina Carpenter'

print(f"Buscando por '{artista_alvo}' no banco de dados...")


df_sabrina = df[df[coluna_artista].str.contains(artista_alvo, case=False, na=False)]

if len(df_sabrina) > 0:
    print(f"Sucesso! Encontramos {len(df_sabrina)} faixas brutas.\n")


    colunas_interesse = [coluna_musica, 'popularity', 'danceability', 'energy', 'valence', 'acousticness']
    colunas_presentes = [col for col in colunas_interesse if col in df.columns]
    

    df_sabrina = df_sabrina[colunas_presentes]
    
    df_sabrina = df_sabrina.drop_duplicates(subset=[coluna_musica])

    print(f"Após a limpeza de duplicatas, restaram {len(df_sabrina)} faixas únicas para análise.\n")

    if 'popularity' in colunas_presentes:
        top_5 = df_sabrina.sort_values(by='popularity', ascending=False).head(5)
        print("--- Top 5 Músicas (por Popularidade) ---")
        print(top_5[[coluna_musica, 'popularity', 'energy', 'danceability']].to_string(index=False))
        print("\n")

    if 'energy' in colunas_presentes and 'danceability' in colunas_presentes:
        media_energia = df_sabrina['energy'].mean()
        media_danca = df_sabrina['danceability'].mean()
        
        musica_mais_dancante = df_sabrina.sort_values(by='danceability', ascending=False).iloc[0]

        print("--- Insights do Perfil Sonoro ---")
        print(f"Média de Energia da discografia: {media_energia:.2f} (escala 0 a 1)")
        print(f"Média de Dançabilidade: {media_danca:.2f} (escala 0 a 1)")
        print(f"Faixa com maior potencial de pista: '{musica_mais_dancante[coluna_musica]}' (Nota: {musica_mais_dancante['danceability']:.2f})\n")

    nome_arquivo_final = 'dados_limpos_sabrina_carpenter.csv'
    df_sabrina.to_csv(nome_arquivo_final, index=False)
    
    print(f"Pipeline concluído! Arquivo salvo como: '{nome_arquivo_final}'.")
    print("Este CSV está pronto para ser importado no Power BI ou Metabase.")

else:
    print(f"Nenhum dado encontrado para '{artista_alvo}'. Verifique o nome da coluna no dataset.")
