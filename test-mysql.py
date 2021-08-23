from sqlalchemy import create_engine, text

connStr = 'mysql+mysqldb://root:terces@0.0.0.0:3306/Activity'

engine = create_engine(connStr, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("Select cadence from DataFrame;"))
    print(result.all())

