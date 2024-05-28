'''
Nomes finais das tabelas:
anime.csv
anime_genero.csv
user_filtered (a mesma tabela do dataset do Kaggle)
user.csv
'''

import pandas as pd

# Carregar os dados do arquivo CSV dos animes
df = pd.read_csv('../anime_dataset/anime-dataset-2023.csv')

# Em anime, só quero incluir as colunas 'anime_id', 'Name', 'Type', 'Episodes', 'Aired' e 'Rating'
anime = df[['anime_id', 'Name', 'Type', 'Episodes', 'Aired', 'Rating']]
# Trocar os valores "UNKNOWN" dos episódios para o FLOAT -1.0. Gera um Warning
anime['Episodes'] = anime['Episodes'].replace('UNKNOWN', -1.0)

# Salvar o novo DataFrame em um novo arquivo CSV
anime.to_csv('anime.csv', index=False)

# Na tabela anime_genres, queremos incluir o 'anime_id' e o 'genres' de forma normalizada
anime_genero = df.set_index('anime_id')['Genres'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)

# Renomear a coluna resultante para 'Gênero'
anime_genero.name = 'Genre'

# Criar um novo DataFrame com IDs e Gêneros
anime_genero_normalizado = anime_genero.reset_index()

# Salvar o novo DataFrame em um novo arquivo CSV
anime_genero_normalizado.to_csv('anime_genero.csv', index=False)

# Carregar os dados do arquivo CSV dos usuários
df = pd.read_csv('../anime_dataset/users-details-2023.csv')

# Em usuários, só quero incluir as colunas 'Mal ID', 'Username', 'Gender', 'Birthday', 'Location'
users = df[['Mal ID', 'Username', 'Gender', 'Birthday', 'Location']]
# Remover aspas simples na coluna 'Location' (causa erros na importação para o PgAdmin)
users['Location'] = users['Location'].str.replace("'", "")

# Salvar o dados dos usuários
users.to_csv('user.csv', index=False)

# Carregar os dados do arquivo CSV da avaliação dos usuários
users_score = pd.read_csv('../anime_dataset/users-score-2023.csv')

# Em users_score, só quero incluir as colunas 'user_id', 'anime_id', 'rating'
users_score = users_score[['user_id', 'anime_id', 'rating']]
# Apagar de users_scores os usuários que não estão na tabela de user (restrição de chave estrangeira)
user_ids = users['Mal ID']
user_score_filtered_fk = users_score[users_score['user_id'].isin(user_ids)]
# Apagar de users_scores os animes que não estão na tabela de animes (restrição de chave estrangeira)
animes_ids = anime['anime_id']
user_score_filtered_fk = user_score_filtered_fk[user_score_filtered_fk['anime_id'].isin(animes_ids)]


# Salvar o novo DataFrame em um novo arquivo CSV
user_score_filtered_fk.to_csv('user_ratings.csv', index=False)
