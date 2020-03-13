CREATE TABLE users (
	id INTEGER PRIMARY KEY,
	email text,
	password text
);

CREATE TABLE novels (
	id INTEGER PRIMARY KEY,
	title text,
	path text,
	unique_id text,
	progress integer,
	user_id integer,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
