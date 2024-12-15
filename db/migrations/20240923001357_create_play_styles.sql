-- migrate:up

CREATE TABLE play_styles (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(30)
);

-- migrate:down

DROP TABLE IF EXISTS play_styles;
