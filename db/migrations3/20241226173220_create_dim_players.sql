-- migrate:up

CREATE TABLE dim_players (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(60),
  sex VARCHAR(10),
  url VARCHAR(120)
);

-- migrate:down

DROP TABLE dim_players;
