CREATE TABLE dim_locations (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  league_name	VARCHAR(80),
  nation_league_name	VARCHAR(80),
  team_name	VARCHAR(80),
  nation VARCHAR(100)
);
CREATE TABLE dim_skills (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  foot	VARCHAR(10),
  position VARCHAR(40),
  extra_positions VARCHAR(200),
  styles	VARCHAR(200)
);
CREATE TABLE dim_players (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(60),
  sex VARCHAR(10),
  url VARCHAR(120)
);
CREATE TABLE fact_events (
    location_id INTEGER,
    player_id INTEGER, -- INTEGEREGER se convierte en INTEGER en SQL Server
    skill_id INTEGER,
    overall INTEGER,
    velocity INTEGER,
    shooting INTEGER,
    passing INTEGER,
    dribbling INTEGER,
    defending INTEGER,
    physicality INTEGER,
    diving INTEGER, -- INTEGEREGER se convierte en INTEGER en SQL Server
    handling INTEGER,
    kicking INTEGER,
    positioning INTEGER,
    reflexes INTEGER,
    skill_moves INTEGER,
    weak_foot INTEGER,
    ranking INTEGER,
    height INTEGER,
    weight INTEGER,
    age INTEGER, -- es la edad de un jugador (dim_players)
    FOREIGN KEY (location_id) REFERENCES dim_locations (id),
    FOREIGN KEY (player_id) REFERENCES dim_players (id),
    FOREIGN KEY (skill_id) REFERENCES dim_skills (id)
);


La edad del jugador (dim_players) se encuentra en la columna age de la tabla fact_events.

el sexo del jugador se encuentra en dim_players y no en fact_events