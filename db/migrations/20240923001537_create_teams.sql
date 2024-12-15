-- migrate:up

CREATE TABLE teams (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  league_id	INTEGER NOT NULL,
  FOREIGN KEY (league_id) REFERENCES leagues (id)
);

-- migrate:down

DROP TABLE IF EXISTS teams;
