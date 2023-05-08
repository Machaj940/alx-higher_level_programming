-- List all shows without the genre comedy

SELECT DISTINCT tv_shows.title
FROM tv_shows LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.genre_id NOT IN (
SELECT tv_show_genres.show_id
FROM tv_show_genres
WHERE tv_genres.name = 'comedy')
ORDER BY tv_shows.title;
