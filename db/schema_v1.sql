CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE play_styles (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(30)
);
CREATE TABLE sexs (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(7)
);
CREATE TABLE nations (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40)
);
CREATE TABLE positions (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);
CREATE TABLE foots (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(6)
);
CREATE TABLE leagues (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(30),
  nation_id	INTEGER,
  FOREIGN KEY (nation_id) REFERENCES nations (id)
);
CREATE TABLE teams (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  league_id	INTEGER NOT NULL,
  FOREIGN KEY (league_id) REFERENCES leagues (id)
);
CREATE TABLE players (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(60),
  rank INTEGER,
  weak_foot INTEGER,
  skill_moves INTEGER,
  heigth INTEGER,
  weight INTEGER,
  age INTEGER,
  url VARCHAR(120),
  foot_id INTEGER NOT NULL,
  sex_id INTEGER NOT NULL,
  position_id INTEGER NOT NULL,
  nation_id	INTEGER NOT NULL,
  team_id	INTEGER NOT NULL,
  FOREIGN KEY (foot_id) REFERENCES foots (id),
  FOREIGN KEY (sex_id) REFERENCES sexs (id),
  FOREIGN KEY (position_id) REFERENCES positions (id),
  FOREIGN KEY (nation_id) REFERENCES nations (id)
  FOREIGN KEY (team_id) REFERENCES teams (id)
);
CREATE TABLE common_details (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  overall INTEGER,
  velocity INTEGER,
  shooting INTEGER,
  passing INTEGER,
  dribbling INTEGER,
  defending INTEGER,
  physicality INTEGER,
  player_id	INTEGER NOT NULL,
  FOREIGN KEY (player_id) REFERENCES players (id)
);
CREATE TABLE goalkeeper_details (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  diving INTEGER,
  handling INTEGER,
  kicking INTEGER,
  positioning INTEGER,
  reflexes INTEGER,
  player_id	INTEGER NOT NULL,
  FOREIGN KEY (player_id) REFERENCES players (id)
);
CREATE TABLE players_play_styles (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  play_style_id	INTEGER NOT NULL,
  player_id	INTEGER NOT NULL,
  FOREIGN KEY (play_style_id) REFERENCES play_styles (id),
  FOREIGN KEY (player_id) REFERENCES players (id)
);
CREATE TABLE players_positions (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  position_id	INTEGER NOT NULL,
  player_id	INTEGER NOT NULL,
  FOREIGN KEY (position_id) REFERENCES positions (id),
  FOREIGN KEY (player_id) REFERENCES players (id)
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20240923001357'),
  ('20240923001430'),
  ('20240923001435'),
  ('20240923001454'),
  ('20240923001519'),
  ('20240923001531'),
  ('20240923001537'),
  ('20240923001538'),
  ('20240923001700'),
  ('20240923001723'),
  ('20240923001817'),
  ('20240923001826'),
  ('20240923014951'),
  ('20240923015353'),
  ('20240923020831'),
  ('20240923023448'),
  ('20240923023547'),
  ('20240923031932'),
  ('20240923052437'),
  ('20240929033656'),
  ('20240929053853'),
  ('20240929054710'),
  ('20240929061027'),
  ('20240929061638');
