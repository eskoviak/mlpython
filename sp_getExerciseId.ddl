DELIMITER //


CREATE PROCEDURE getExerciseId( IN exerciseNm VARCHAR(50), OUT eid INT)
BEGIN
    SELECT id INTO eid FROM Exercises WHERE exerciseName = exerciseNm;
END//

DELIMITER ;