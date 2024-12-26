-- migrate:up

CREATE TABLE players_positions (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  position_id	INTEGER NOT NULL,
  player_id	INTEGER NOT NULL,
  FOREIGN KEY (position_id) REFERENCES positions (id),
  FOREIGN KEY (player_id) REFERENCES players (id)
);

-- migrate:down

DROP TABLE IF EXISTS players_positions;
