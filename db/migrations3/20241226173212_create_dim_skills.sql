-- migrate:up

CREATE TABLE dim_skills (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  foot	VARCHAR(10),
  position VARCHAR(40),
  extra_positions VARCHAR(200),
  styles	VARCHAR(200)
);

-- migrate:down

DROP TABLE dim_skills;