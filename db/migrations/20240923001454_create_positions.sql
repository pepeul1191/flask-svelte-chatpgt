-- migrate:up

CREATE TABLE positions (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);

-- migrate:down

DROP TABLE IF EXISTS positions;
