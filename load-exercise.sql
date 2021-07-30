create table if not exists Exercises (
    id              int auto_increment primary key,
    exerciseName    varchar(40) not null
);

truncate table Exercises;

insert into Exercises (exerciseName)
values ('Bulgarian Split Squat'),
('Overhead BB Press'),
('Pendlay Row'),
('SL KB RDL'),
('Deadlift'),
('Zercher Sq'),
('Kneeling Landmine Pr'),
('SA Bench Row'),
('Farmers Carry'),
('Bench Press'),
('Front Squat'),
('EZ Bicep Curl'),
('SA Farmer Carry'),
('Rear Squat'),
('Power Clean'),
('Rear Deltoid'),
('Hanging Leg Raise'),
('Sumo Deadlift'),
('Pull Up'),
('Dips'),
('Weighted Step Up');
