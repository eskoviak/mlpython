from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, declarative_base, registry, relationship
from sqlalchemy.sql.expression import column, null

Base = declarative_base()
mapper_registry = registry()

strConn = 'mysql+mysqldb://root:terces@0.0.0.0:3306/test'
engine = create_engine(strConn, echo=True, future=True)

'''Old Way
r_table = Table(
   "user_account",
    mapper_registry.metadata,
    Column('id',Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String(50))
)

address_table = Table(
    "address",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String(50), nullable=False)
)

mapper_registry.metadata.create_all(engine)
'''
class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(50))

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id',))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r}"

Base.metadata.create_all(engine)