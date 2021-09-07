
SET @intensity = 'High Intensity';
SET @exercise = 'Bench Press';

SELECT date, exerciseName,cadence,weights
FROM WeightLifting w JOIN Exercises e ON e.id = w.exerciseId JOIN Categories c ON c.id = w.categoryId
WHERE e.exerciseName = 'Overhead BB Press'
  AND c.categoryName = 'High Intensity'
ORDER BY exerciseName, date;
