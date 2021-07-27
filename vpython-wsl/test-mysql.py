from sqlalchemy import create_engine, text

connStr = 'mysql+mysqldb://root:terces@127.0.0.1:3306/test'

engine = create_engine(connStr, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("Select 'hello world'"))
    print(result.all())

