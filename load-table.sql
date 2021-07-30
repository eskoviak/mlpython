load data local infile 'loadfile.csv'
  into table WeightLifting
        fields terminated by ','
        ignore 1 lines
	(Date,ExerciseId,CategoryId,Cadence,Weights,WeightUnit,Comments)

