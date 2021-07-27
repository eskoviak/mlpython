from sqlalchemy import create_engine, text

url = 'postgresql+psycopg2://ed:Kh4V3R9B7DcygecH@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/bank?sslmode=verify-full&sslrootcert=.postgresql\\root.crt&options=--cluster%3Dgolden-dingo-2123'

engine = create_engine(url)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'hello ed'"))
    print(result.all())
    

