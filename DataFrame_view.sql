CREATE VIEW DataFrame (
	date,
	exercise,
	category,
	cadence,
	weights
) AS
	SELECT date,exerciseName,categoryName,cadence,weights
	FROM WeightLifting w
	JOIN Categories c ON c.id = w.categoryId
	JOIN Exercises e on e.id = w.exerciseId
	ORDER BY date, categoryId
