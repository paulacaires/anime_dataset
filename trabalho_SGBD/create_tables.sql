/* 'anime_id', 'Name', 'Type', 'Episodes', 'Aired', 'Rating' */
CREATE TABLE anime (
	anime_id 	INTEGER PRIMARY KEY NOT NULL,
	anime_name	VARCHAR(500) NOT NULL,
	anime_type	VARCHAR(255),
	aired 		VARCHAR(255),
	score 		FLOAT	
);

/* 'anime_id' e o 'genres' */
CREATE TABLE anime_genero (
	anime_id	INTEGER,
	genre		VARCHAR(255),
	CONSTRAINT fk_animeID_animeGenero FOREIGN KEY (anime_id) REFERENCES anime(anime_id)		
);
	
/* Mal ID', 'Username', 'Gender', 'Birthday', 'Location' */
CREATE TABLE mal_user ( /* My Anime List User */
	user_id INTEGER PRIMARY KEY NOT NULL,
	username VARCHAR(255) NOT NULL,
	gender VARCHAR(255),
	birthday VARCHAR(255),
	location VARCHAR(255)
);

/* Igual à tabela user_filtered */
CREATE TABLE user_rating (
	user_id		INTEGER UNIQUE NOT NULL,
	anime_id	INTEGER UNIQUE NOT NULL,
	rating 		FLOAT,
	CONSTRAINT fk_userID_userRating FOREIGN KEY (user_id) REFERENCES mal_user(user_id),
	CONSTRAINT fk_animeID_userRating FOREIGN KEY (anime_id) REFERENCES anime(anime_id)
);
