-- script that displays the top 3  temperature (Fahrenheit) of dities temp
--  during july and august ordered by temperature (descending)

SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp desc LIMIT 3;
