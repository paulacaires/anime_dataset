CREATE TABLE anime_dataset (
	anime_id INTEGER PRIMARY KEY,
	anime_name VARCHAR[100] NOT NULL,
	english_name VARCHAR[100],
	other_name VARCHAR[100],
	/* três digitos no total, sendo 2 decimais */
	score DECIMAL(3, 2), 
	genres VARCHAR[100],
	synopsis VARCHAR[1000],
	anime_type VARCHAR[100],
	/* cinco dígitos no total, sendo 1 decimal (por exemplo, um anime pode ter 1000.0 episódios) */
	episodes DECIMAL(5,1),
	aired VARCHAR[100],
	premiered VARCHAR[100],
	status VARCHAR[100],
	producers VARCHAR[500],
	licensors VARCHAR[500], 
	studios VARCHAR[100],
	source_material VARCHAR[100],
	duration VARCHAR[100],
	rating VARCHAR[100], 
	anime_rank DECIMAL(5,1),
	popularity INTEGER,
	favorites INTEGER,
	scored_by DECIMAL(10,1),
	members INTEGER,
	image_URL VARCHAR[100]
);

