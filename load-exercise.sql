create table if not exists Exercises (
    id              int auto_increment primary key,
    exerciseName    varchar(40) not null,
	description		text null
);

truncate table Exercises;

insert into Exercises (exerciseName, description)
values ('Bulgarian Split Squat',''),
('Overhead BB Press','')
('Pendlay Row',''),
('SL KB RDL',''),
('Deadlift',''),
('Zercher Sq',''),
('Kneeling Landmine Pr',''),
('SA Bench Row',''),
('Farmers Carry',''),
('Bench Press',''),
('Front Squat',''),
('EZ Bicep Curl',''),
('SA Farmer Carry',''),
('Rear Squat',''),
('Power Clean',''),
('Rear Deltoid',''),
('Hanging Leg Raise',''),
('Sumo Deadlift',''),
('Pull Up',''),
('Dips',''),
('Weighted Step Up',''),
('Ladder - Clean/Press','This is performed by doing 1 clean, followed by doing the specified press (string, push or snatch)'),
('Two Hand KB Swing',''),
('Ladder -- Goblet Squat',''),
('Floor Press','')
;
