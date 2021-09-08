from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, registry, declarative_base, relationship
from sqlalchemy.schema import Table
import json

#with open('Weight History/input.json', 'r') as f:
#    inputjson  = json.load(f)
    
#print (inputjson)

connStr = 'mysql+mysqldb://root:terces@0.0.0.0:3306/Activity'
engine = create_engine(connStr, echo=True)

Base = declarative_base()
mapper_registry = registry()

exercises = Table("Exercises", mapper_registry.metadata, autoload_with=engine)
categories = Table("Categories", mapper_registry.metadata, autoload_with=engine)
weightLifting = Table("WeightLifting_dev", mapper_registry.metadata, autoload_with=engine)

class Exercises(Base):
    __table__ = exercises

    #weightLifting = relationship("WeightLifting", back_populates="exercise")
    
    def __repr__(self):
        return f"Exercises(id={self.id!r}, exerciseName={self.exerciseName!r}, description={self.description!r})"
    
class Categories(Base):
    __table__ = categories

    #weightLifting = relationship("WeightLifting", back_populates="category")

    def __repr__(self):
        return f"Categories(id={self.id!r}, categoryName={self.categoryName!r}"

class WeightLifting(Base):
    __table__ = weightLifting

    #category = relationship("Categories", back_populates="weightLifting")
    #exercise = relationship("Exercises", back_populates="weightLifting")

    def __repr__(self):
        return f"WeightLifting(date: {self.date!r}, Exercise: {self.exercise!r} )"


with Session(engine) as session:
    stmt = select(Categories)
    print(stmt)
    for row in session.execute(stmt):
        print(row)
    session.commit()
