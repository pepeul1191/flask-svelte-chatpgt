-- migrate:up

CREATE TABLE foots (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(6)
);

-- migrate:down

DROP TABLE IF EXISTS foots;
