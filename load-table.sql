load data local infile 'loadfile.csv'
  into table WeightLifting
        fields terminated by ',' optionally enclosed by '"'
        ignore 1 lines
	(
	Date,
	@exerciseName,
	@categoryName,
	Cadence,
	Weights,
	WeightUnit,
	Comments
	)
	set exerciseId = (select id from Exercises where exerciseName = @exerciseName),
	categoryId = (select id from Categories where categoryName = @categoryName)
	;

