-- migrate:up

CREATE TABLE nations (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40)
);

-- migrate:down

DROP TABLE IF EXISTS nations;
