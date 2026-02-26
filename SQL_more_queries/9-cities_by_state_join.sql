-- listing cities and states
SELECT cities.id, cities.name, states.name
FROM cities
inner JOIN states
ON cities.state_id = states.id
ORDER BY cities.id;
