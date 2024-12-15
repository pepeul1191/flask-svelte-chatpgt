-- migrate:up

CREATE TABLE players (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  rank INTEGER,
  name VARCHAR(50),
  overall INTEGER,
  velocity INTEGER,
  shooting INTEGER,
  passing INTEGER,
  dribbling INTEGER,
  defending INTEGER,
  physicality INTEGER,
  position VARCHAR(50),
  weak_foot INTEGER,
  skill_moves INTEGER,
  preferred_foot VARCHAR(50),
  height INTEGER,
  weight INTEGER,
  alternative_positions VARCHAR(50),
  age INTEGER,
  nation VARCHAR(50),
  league VARCHAR(50),
  team VARCHAR(50),
  play_styles VARCHAR(50),
  url VARCHAR(120),
  diving INTEGER,
  handling INTEGER,
  kicking INTEGER,
  positioning INTEGER,
  reflexes INTEGER,
  sex VARCHAR(10)
);

-- migrate:down

DROPT TABLE players;

{skill_moves}, {heigth}, {weight}, {url}, {foot_id}, {sex_id}, {position_id}, {nation_id}, {team_id}, {age}