## Base de Datos

Instalar y activar el ambiente virtual - Linux:

    $ sudo apt install python3-virtualenv python3-venv
    $ python3 -m venv ./env
    $ source env/bin/activate

Instalar y activar el ambiente virtual - Windows:

    > pip install virtualenv
    > virtualenv env
    > env\Scripts\activate.bat

Arrancar aplicación:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ mkdir static/uploads
    $ python main.py

## Migraciones

Archivo <b>.env</b>

    OPENAI_API_KEY=XYZ
    OPENAI_API=false||true
    DB1=sqlite3:db/fifa25v1.db
    DB2=sqlite3:db/fifa25v2.db
    DB3=sqlite3:db/fifa25v3.db
    DB_VERSION=1||2|||3
    ENV=local

Migraciones con DBMATE - app:

    $ dbmate -d "db/migrations" -e "DB" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DB" up
    $ dbmate -d "db/migrations" -e "DB" rollback

Migraciones con DBMATE - app2:

    $ dbmate -d "db/migrations" -e "DB2" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DB2" up
    $ dbmate -d "db/migrations" -e "DB2" rollback

Backup SQLite

    $ sqlite3 app.db .dump > dbname.bak

Ejecutar la aplicación con Gunicorn:

    $ gunicorn app:APP -w 6 -b 0.0.0.0:5000 --reload

MongoDB:

    $ sudo chown -R mongodb:mongodb /var/lib/mongodb
    $ sudo chown mongodb:mongodb /tmp/mongodb-27017.sock
    $ sudo chown -R mongodb:mongodb /var/log/mongodb
    $ sudo systemctl start mongod
    $ sudo ss -pnltu | grep 27017
    $ mongosh

Consultas MongoDB:

Fetch all a un resumen de todas las conversaciones de un usuario por usuario_id:

```javascript
db.conversations.aggregate([
  {
    "$match": {
      "user_id": ObjectId(usuario_id) // Reemplaza con el ObjectId que deseas filtrar
    }
  },
  {
    $lookup: {
      from: "messages", // Nombre de la colección de destino
      localField: "messages", // Campo en la colección de `conversations`
      foreignField: "_id", // Campo en la colección de `messages`
      as: "message_details" // Nombre del campo de salida que contendrá los documentos unidos
    }
  },
  {
    "$project": {
      "_id": { "$toString": "$_id" },
      "name": 1,
      "created_at": 1,
      "updated_at": 1,
      "message_count": { $size: "$message_details" }
    }
  }]);
```

Fetch a una conversación:

```javascript
db.conversations.aggregate([
  {
    "$match": {
      "_id": ObjectId("67086aa7fecae0b7e7381844")
    }
  },
  {
    "$lookup": {
      "from": "messages",
      "localField": "messages",
      "foreignField": "_id",
      "as": "message_details"
    }
  },
  {
    "$unwind": {
      "path": "$message_details",
      "preserveNullAndEmptyArrays": true
    }
  },
  {
    "$group": {
      "_id": {
        "conversation_id": "$_id",
        "name": "$name",
        "created_at": {
          "$dateToString": {
            "format": "%d/%m/%Y %H:%M:%S",
            "date": "$created_at"
          }
        },
        "updated_at": {
          "$dateToString": {
            "format": "%d/%m/%Y %H:%M:%S",
            "date": "$updated_at"
          }
        }
      },
      "messages": {
        "$push": {
          "answer": {
            "columns": "$message_details.answer.columns",
            "result_set": "$message_details.answer.result_set",
            "query": "$message_details.answer.query",
            "_id": { "$toString": "$message_details.answer._id" }
          },
          "error": "$message_details.error",
          "question": "$message_details.question",
          "created_at": {
            "$dateToString": {
              "format": "%d/%m/%Y %H:%M:%S",
              "date": "$message_details.created_at"
            }
          }
        }
      }
    }
  },
  {
    "$project": {
      "_id": 0,
      "id": { "$toString": "$_id.conversation_id"},  // Renombramos a `id`
      "name": "$_id.name",
      "created_at": "$_id.created_at",
      "updated_at": "$_id.updated_at",
      "messages": 1
    }
  },
  {
    "$limit": 1
  }
]);
```

# Base de Datos v1

Diagrama de Base de Datos

![Diagrama de Base de Datos v1](https://planttext.com/plantuml/png/dLRRQi9047tVhrZoqWielT62Y2Z5NYYK8gMlOJLZicHp8RjQfVhltIIRc6oYINmHd3apP-RipEYO2nA9bSSG0bzGiSKX8rkJYoq3ZlyGnjUOMdY0tp-_fw_J6HuElpv68sdlzUI7JpoGpf_9xFbjChkylxb2-pmJXqtt54_533uHDF2x9taerH46d9wNvxQKPna4edkEns8A1iHUdIaiLdAOMjXB77QW442yynJ3ghm6WdX083f3Y8GY8hvxY926No2k6KjRidANCcPwmLgALRGxG6r7Q0ag9c93wVigOiLNlKigYJbhMyNnv1xnPBDqn7tYXN3oCWtQBWBFa_4M249P2ucbFX5XhDJi6bYmY9ELz7HajzItIyQGSAxRh8ZEvwnYXINuLYNUsNAw84mdIoUaeLKx8Cm522MmTRiMNUirECItAkMwTE5MYbKlfziZM3BOQ6FMgWEr26QdYta07vkmJjJjJrl3v9wclS0pOEanTcZ8KNR7zhj-VxVBx_G06_a662YzH0gIHKX8VcKCbDqI1Kelh8IetQm0afyKwKyNjE8-o24nXOOhmFg2DL1QluIenJMGjfuPgmgBEJCL3LGptoVnTTDK2CXCAYWVeSR04qovMctbgmcfPK1ZUItaduf_)


# Base de Datos v2

Diagrama de Base de Datos

![Diagrama de Base de Datos v2](https://planttext.com/plantuml/png/PP9DZiCW38NtEGNdwAetGMvmWXK78kpGHgEv-r1rQ9sPdJ__wVd1LHIAxYiF0oObFTp6S60HzpKuH-7YA6cB2gIbnmbMlBWAPOnG6Wi-BEQA1PXxTqNEOrlSMMBEIcdkl868mL3eTcERm0bJi0Fn41g1pSuj2odbP6K0AvO4IXLzhujjk2CiVcfYtieMOlPhqoyzzIf_PYBI7Dy3znF1Z1-7_gfXX7a_kVRgyVyBYh1QVZw85pqOJ_BtmXO3LUDHX1IiYGkDYxNmrm-JAZWnFlhbtyDmRQwtV_43)


# Base de Datos v3

Diagrama de Base de Datos

![Diagrama de Base de Datos v3](https://planttext.com/plantuml/png/VLDDRuCm3BtpApXkbwghfcdYr7yIkSI0XGbL4XXexBylvTCWjRVu-Vd5VawkpeFrJSLHXCQJxsDDbU8w1K-rSV5l5CUaavYC3oT6o1jK1YfCuXPiMe1z-pw_XvGP2zGBXaUeNfHkwCSvm7-xXbn9pCTkihhsikgXTQyTxTK-HnmxRq4jMRUbB-SnxtpFU8JtFTmPUhJ79lO3VKrYs1txQYmBwB8Jpo3r2jiGJUAB-sgxPRfR0ACX8gvRjC2yX2q6aQ2zqelW5PbyrGFdHAWjtMui0SpGQ5bGz8vIOA6fgHM40eoM2YMbfQoVdHUGnOonUvWkHwh292lqWr2gQSrp3HYfMY3bXT_OCe8SfsCmMZey3AVJC1oUUI9DVqPV7a2ohUCPTNwloRgdABe6GyC_-mS0)

Diagrama de Secuencia al realizar preguntas.

![Diagrama de Secuencia al realizar pregunta](https://planttext.com/plantuml/png/PLFDJW8n4BxtAIQSD4OJzyZ12886iu92l7aPbX6BfQtzsUX3UV8HV36dXOL5JfljzpUTcLxxW2x4jH9O1UFWsKTqqWZBfxAI5dM0pgmc5QXdRGVGm-tq47ty2cz6mwr2_vu9_U4_-LCf0y6Wdz51__8GVZ1wQVPeiQsaCx6aUwDyEkcDXDYM1kTNN09qOUWh9-S4rj4owe199sla9AxmYAphts_SSO4ql6WeIIyZhWZ66A931IVb-5ImW6Nz8SiU6tuvtjlp_SJIcMZXnX4wk34wq6Smi2352hEsGK3IDoub4VZgZTPuuJ_KCIQr9nVyCNYVitT5LzncXQbmgL-DMsCbVtyqnu8o7fAQz4A8ZG7tZ1rsjPqTt6L_cKG3JatV9fP5FYfcykJ4WjhSbf87cPMRkFJ7RLvH5NcZKgbx2yXeupwbXC2C0fnCPwVjWBGRxO2YPLzquSxXlErz1jDPDYzsvfFvYa8rMXow5arJCkUED3a4Hzwo4ssmPb46L4TIDMKu4Z-FjXMFFcq7avi5wy93OctzZWIyYkAQfy8lx0y0=)

Preguntas de ejemplo:

+ lista de miembros
+ nombres de ejercisios y cantidad de ejercicios asignados a cuantos miembros agrupados por ejercicio

---

Fuentes:

+ https://chat.openai.com/c/605a221a-87d7-4798-8783-37ecd465e384
+ https://github.com/sulmanweb/openai_chatgpt
+ https://www.cherryservers.com/blog/install-mongodb-ubuntu-22-04
+ https://regex101.com/r/rbf4KT/1