CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE players (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  rank INTEGER,
  name VARCHAR(50),
  sex VARCHAR(10),
  overall INTEGER,
  velocity INTEGER,
  shooting INTEGER,
  passing INTEGER,
  dribbling INTEGER,
  defending INTEGER,
  physicality INTEGER,
  position VARCHAR(50),
  alternative_positions VARCHAR(50),
  weak_foot INTEGER,
  skill_moves INTEGER,
  foot VARCHAR(50),
  height INTEGER,
  weight INTEGER,
  age INTEGER,
  nation VARCHAR(50),
  league VARCHAR(50),
  nation_league VARCHAR(50),
  team VARCHAR(50),
  play_styles VARCHAR(50),
  url VARCHAR(120),
  diving INTEGER,
  handling INTEGER,
  kicking INTEGER,
  positioning INTEGER,
  reflexes INTEGER
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20241215042500'),
  ('20241215140537');
