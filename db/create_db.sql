CREATE TABLE IF NOT EXISTS photos (
    album_id        integer,
    data            integer,
    id              integer PRIMARY KEY,
    owner_id        char(30),
    image           bytea
                    );