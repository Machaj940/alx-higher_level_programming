-- List all genres of the show Dexter

SELECT tv_genres.name
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.genre_id = tv_shows.id
WHERE tv_show_genres.show_id = (
SELECT tv_shows.id
FROM tv_shows
WhERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
