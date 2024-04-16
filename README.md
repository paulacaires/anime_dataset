# anime_dataset

Link do Kaggle:
https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset/data?select=anime-dataset-2023.csv

Como as tabelas foram importadas para o PgAdmin:
https://www.youtube.com/watch?v=UdMj8iKSCoc


## Preparação do Ambiente

1. Fazer Download da pasta do Kaggle, descompactar e renomear a pasta com os dados CVS de ```anime_dataset```. Essa pasta tem que ficar na mesma pasta que a pasta ```trabalho_SGBD```, onde ficarão todos os códigos.
2. Instalar Python
3. Instalar Pandas pelo comando
   ```sudo apt install python3-pandas```


## Normalização

No dataset original, existe nas tabelas que referenciam animes um atributo multivalorado dos `genres`.

 ![Ilustrando o atributo multivalorado](/img/1.png) .

A solução foi escrever no script instruções que criam uma nova tabela `anime_genre.csv` com duas colunas: ID e gênero. 

## Tabelas

`anime.csv`: De `anime_dataset`, tem as informações dos animes
- 'anime_id', 'Name', 'Type', 'Episodes', 'Aired' e 'Rating'

`anime_genero.csv`: De `anime_dataset`, tem as categorias dos animes
- 'anime_id' e 'genre'

`user_filtered.csv`: Para ter a nota que cada usuário deu pros animes. Não é criada no script porque tem muitas tuplas, por isso é exatamente igual ao do dataset no Kaggle.

User: de user_details, informações dos usuários
malID, username, gender, birthday, location 

## Consultas

Usuários mais velhos tendem a dar notas mais altas para animes mais antigos?

Qual é a nota média que usuários com mais de 30 anos dão para os animes atuais?
