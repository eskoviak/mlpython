SELECT * INTO OUTFILE '/var/lib/mysql/WeightLifting.csv' 
  FIELDS TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM DataFrame
  ORDER BY date;

SELECT exerciseName, description INTO OUTFILE '/var/lib/mysql/Exercises.csv'
  FIELDS TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM Exercises
  ORDER BY exerciseName;

SELECT categoryName INTO OUTFILE '/var/lib/mysql/Categories.csv'
  FIELDS TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM Categories;
