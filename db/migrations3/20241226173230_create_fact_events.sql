-- migrate:up

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
    age INTEGER,
    FOREIGN KEY (location_id) REFERENCES dim_locations (id),
    FOREIGN KEY (player_id) REFERENCES dim_players (id),
    FOREIGN KEY (skill_id) REFERENCES dim_skills (id)
);

-- migrate:down

DROP TABLE fact_events;