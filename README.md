# anime_dataset

Link do Kaggle dos dados originais, sem os tratamentos aplicados:
https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset/data?select=anime-dataset-2023.csv

Como as tabelas foram importadas para o PgAdmin:
https://www.youtube.com/watch?v=UdMj8iKSCoc


## Preparação do Ambiente

1. Fazer Download da pasta do Kaggle, descompactar e renomear a pasta com os dados CVS de `anime_dataset`. Essa pasta tem que ficar na mesma pasta que a pasta `trabalho_SGBD`, onde ficarão todos os códigos. Não é uma dentro da outra, e sim as duas separadas no mesmo lugar. Ou seja, ambas as pastas tem que estar em `Documentos` por exemplo. 
2. Instalar Python
3. Instalar Pandas pelo comando
   `sudo apt install python3-pandas`
4. Ir para a pasta `trabalho_SGBD` (utilizando o comando `cd`) e rodar o comando: `python3 creating_csv.py`


## Normalização

No dataset original, existe nas tabelas que referenciam animes um atributo multivalorado dos `genres`.

 ![Ilustrando o atributo multivalorado](/img/1.png)

A solução foi escrever no script instruções que criam uma nova tabela `anime_genre.csv` com duas colunas: ID e gênero. 

## Tabelas

`anime.csv`: De `anime_dataset`, tem as informações dos animes
- 'anime_id', 'Name', 'Type', 'Episodes', 'Aired' e 'Score' (antigo rating)

`anime_genero.csv`: De `anime_dataset`, tem as categorias dos animes
- 'anime_id' e 'genre'

`user_rating.csv`: Para ter a nota que cada usuário deu pros animes. De `users-score-2023.csv`.
- 'user_id', 'anime_id', 'score'

`user`: de user_details, informações dos usuários
malID, username, gender, birthday, location 

## CSV files into PostgreSQL
Seguir o tutorial [desse vídeo]([/img/1.png](https://www.youtube.com/watch?v=UdMj8iKSCoc)). 
Os script para a criação das tabelas estão dentro da pasta `trabalho_SGBD`.
