CREATE PROCEDURE Activity.sp_fixcadence()
BEGIN
	
  DECLARE id int;
  DECLARE cadence varchar(50);
  DECLARE done int DEFAULT FALSE;

  DECLARE cadence CURSOR FOR
    SELECT id,cadence 
    FROM WeightLifting
    WHERE cadence NOT LIKE ('%(%');

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  
  OPEN cadence;

  read_loop: LOOP
    FETCH cadence INTO id, cadence;
    IF done THEN 
      LEAVE read_loop;
    END IF;

    SELECT CONCAT('(',cadence,')');
  END LOOP;

  CLOSE cadence;
END;

