TABLE WeightLifting ORDER BY date
  INTO OUTFILE './WeightLifiting.dat'
  FIELDS TERMNIATED BY ','
  OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'