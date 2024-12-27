# Base de Datos v1

Diagrama de Base de Datos

```plantuml
@startuml

entity play_styles {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(30)
}

entity sexs {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(7)
}

entity nations {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(40)
}

entity positions {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(10)
}

entity foots {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(6)
}

entity leagues {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(30)
  nation_id : INTEGER <<FK>>
}

entity teams {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(40)
  league_id : INTEGER <<FK>>
}

entity players {
  * id : INTEGER <<PK>>
  --
  name : VARCHAR(60)
  rank : INTEGER
  weak_foot : INTEGER
  skill_moves : INTEGER
  height : INTEGER
  weight : INTEGER
  age : INTEGER
  url : VARCHAR(120)
  foot_id : INTEGER <<FK>>
  sex_id : INTEGER <<FK>>
  position_id : INTEGER <<FK>>
  nation_id : INTEGER <<FK>>
  team_id : INTEGER <<FK>>
}

entity common_details {
  * id : INTEGER <<PK>>
  --
  overall : INTEGER
  velocity : INTEGER
  shooting : INTEGER
  passing : INTEGER
  dribbling : INTEGER
  defending : INTEGER
  physicality : INTEGER
  player_id : INTEGER <<FK>>
}

entity goalkeeper_details {
  * id : INTEGER <<PK>>
  --
  diving : INTEGER
  handling : INTEGER
  kicking : INTEGER
  positioning : INTEGER
  reflexes : INTEGER
  player_id : INTEGER <<FK>>
}

entity players_play_styles {
  * id : INTEGER <<PK>>
  --
  play_style_id : INTEGER <<FK>>
  player_id : INTEGER <<FK>>
}

entity players_positions {
  * id : INTEGER <<PK>>
  --
  position_id : INTEGER <<FK>>
  player_id : INTEGER <<FK>>
}

' Relationships
leagues }|..|| nations : "nation_id"
teams }|..|| leagues : "league_id"
players }|..|| foots : "foot_id"
players }|..|| sexs : "sex_id"
players }|..|| positions : "position_id"
players }|..|| nations : "nation_id"
players }|..|| teams : "team_id"
common_details }|..|| players : "player_id"
goalkeeper_details }|..|| players : "player_id"
players_play_styles }|..|| play_styles : "play_style_id"
players_play_styles }|..|| players : "player_id"
players_positions }|..|| positions : "position_id"
players_positions }|..|| players : "player_id"

@enduml
```

# Base de Datos v2

Diagrama de Base de Datos

```plantuml
@startuml

entity players {
  id: int
  rank: int
  name: varchar
  sex: varchar
  overall: int
  velocity: int
  shooting: int
  passing: int
  dribbling: int
  defending: int
  physicality: int
  position: varchar
  alternative_positions: varchar
  weak_foot: int
  skill_moves: int
  foot: varchar
  height: int
  weight: int
  age: int
  nation: varchar
  league: varchar
  nation_league: varchar
  team: varchar
  play_styles: varchar
  url: varchar
  diving: int
  handling: int
  kicking: int
  positioning: int
  reflexes: int
}

@enduml
```

# Base de Datos v3

Diagrama de Base de Datos

```plantuml
@startuml

entity dim_locations {
  id: int
  league_name: varchar(80)
  nation_league_name: varchar(80)
  team_name: varchar(80)
  nation: varchar(100)
}

entity dim_skills {
  id: int
  foot: varchar(10)
  position: varchar(40)
  extra_positions: varchar(200)
  styles: varchar(200)
}

entity dim_players {
  id: int
  name: varchar(60)
  sex: varchar(10)
  url: varchar(120)
}

entity fact_events {
  location_id: int
  player_id: int
  skill_id: int
  overall: int
  velocity: int
  shooting: int
  passing: int
  dribbling: int
  defending: int
  physicality: int
  diving: int
  handling: int
  kicking: int
  positioning: int
  reflexes: int
  skill_moves: int
  weak_foot: int
  ranking: int
  height: int
  weight: int
  age: int
}

fact_events ||..|| dim_locations : location_id
fact_events ||..|| dim_players : player_id
fact_events ||..|| dim_skills : skill_id

@enduml
```

# Diagrama de Secuencia

```plantuml
@startuml
actor Usuario
participant "SvelteApp" as FR
participant "Python Flask" as BE
participant "SQLite DB" as DB1
participant "Mongo DB" as DB2
actor "OpenAI" as OAI

Usuario -> FR : Escribe pregunta
activate FR
Usuario -> FR : Envía pregunta en \n Lenguaje Natural (LN)
FR -> BE : Pregunta LN
activate BE

group Crear Contexto del Prompt
  BE -> BE : Lee schema.sql
  BE -> BE : Lee inserts.sql
  BE -> BE : Junta pregunta con la \n información de los sql
end

BE -> OAI : Contexto + Pregunta LN

activate OAI  
  OAI -> BE : Consulta SQL
deactivate OAI

activate DB1  
  BE -> DB1 : Ejecutar consulta SQL
  DB1 -> BE : Result Set (RS)
deactivate DB1

activate DB2
  BE -> DB2: Grabar consulta + RS
  DB2 -> BE : ObjetcId
deactivate DB2

BE -> BE : Genera response

BE --> FR : Devuelve respuesta
deactivate BE
FR --> Usuario : Muestra respuesta
deactivate FR

@enduml