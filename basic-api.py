from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, registry, declarative_base, relationship
from sqlalchemy.schema import Table

## Server
app = Flask(__name__)
api = Api(app)

## Database
Base = declarative_base()
mapper_registry = registry()
connStr = 'mysql+mysqldb://root:terces@0.0.0.0:3306/Activity'
engine = create_engine(connStr, echo=True)
categories = Table("Categories", mapper_registry.metadata, autoload_with=engine)

## Internal Resouces
class Categories(Base):
    __table__ = categories

    #weightLifting = relationship("WeightLifting", back_populates="category")

    def __repr__(self):
        return f"Categories(id={self.id!r}, categoryName={self.categoryName!r}"

## External Resources
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

## Routes
api.add_resource(HelloWorld, '/')
#api.add_resource(Categories, '/categories')        

if __name__ == '__main__':
    app.run(debug=True, port=5100)