from sqlalchemy import create_engine, text

connStr = 'mysql+mysqldb://root:terces@127.0.0.1:3306/Activity'

categoriesDDL = '''
create table if not exists Categories (
    id              int auto_increment primary key,
    categoryName    varchar(40) not null
);

truncate table Categories;

insert into Categories (categoryName)
values ('High Intensity'),('Medium Intensity'),('Low Intensity');

'''

exercisesDDL = '''
create table if not exists Exercises (
    id              int auto_increment primary key,
    exerciseName    varchar(40) not null
0;

truncate table Exercises;

insert into Exercises (exerciseName)
values (''),
(''),
(''),

'''

weightLiftingDDL = '''
Create table WeightLifting ( 
     Id   int AUTO_INCREMENT PRIMARY KEY 
    ,date  datetime NOT NULL 
    ,exerciseId int NOT NULL 
    ,category int NOT NULL 
    ,cadence varchar(40) NOT NULL 
    ,weights varchar(50) NOT NULL 
    ,weightUnit char(3)  default 'lb' 
    ,comments varchar(255) 
    ,CONSTRAINT FOREIGN KEY fk_weightLifting_exercise (exerciseId) REFERENCES Exercises (Id) 
    ,CONSTRAINT FOREIGN KEY fk_weightLifting_category (categoryId) REFERENCES Categories (Id) 
); 
'''
engine = create_engine(connStr, echo=True)

with engine.connect() as conn:
    conn.execute(text(categoriesDDL))
