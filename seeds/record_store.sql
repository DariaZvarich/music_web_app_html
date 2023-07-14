-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;

-- Then, we recreate them
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INTEGER,
    artist_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);