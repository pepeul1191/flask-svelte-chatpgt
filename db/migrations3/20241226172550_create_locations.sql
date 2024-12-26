-- migrate:up

CREATE TABLE dim_locations (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  league_name	VARCHAR(80),
  nation_league_name	VARCHAR(80),
  team_name	VARCHAR(80),
  nation VARCHAR(100)
);

-- migrate:down

DROP TABLE dim_locations;
