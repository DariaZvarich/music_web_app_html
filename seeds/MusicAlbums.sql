DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;



CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int,
    artist_id int
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Born in the U.S.A.', 1984, 1); ---# artist: Bruce Springsteen

INSERT INTO artists (name, genre) VALUES ('Pixies', 'Alternative Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop'); 
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');