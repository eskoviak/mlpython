from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, registry, declarative_base
from sqlalchemy.schema import Table

connStr = 'mysql+mysqldb://root:terces@0.0.0.0:3306/Activity'
engine = create_engine(connStr, echo=True)

Base = declarative_base()
mapper_registry = registry()

exercises = Table("Exercises", mapper_registry.metadata, autoload_with=engine)
categories = Table("Categories", mapper_registry.metadata, autoload_with=engine)

class Exercises(Base):
    __table__ = exercises

    def __repr__(self):
        return f"Exercises(id={self.id!r}, exerciseName={self.exerciseName!r}, description={self.description!r})"

#dictExercises = dict()
with Session(engine) as session:
    for row in session.execute(select(Exercises).where(Exercises.exerciseName == 'EZ Bar Pullover')):
        print(row)
    session.commit()

#print(dictExercises)