-- migrate:up

CREATE TABLE leagues (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(30),
  nation_id	INTEGER,
  FOREIGN KEY (nation_id) REFERENCES nations (id)
);

-- migrate:down

DROP TABLE IF EXISTS leagues;
