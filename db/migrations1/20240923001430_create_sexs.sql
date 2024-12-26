-- migrate:up

CREATE TABLE sexs (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(7)
);

-- migrate:down

DROP TABLE IF EXISTS sexs;
