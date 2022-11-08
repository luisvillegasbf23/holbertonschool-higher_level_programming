-- Import the database dump from hbtn_0d_tvshows
SELECT tv_genres.name genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
