import pandas as pd

connStr = 'mysql+mysqldb://root:terces@0.0.0.0:3306/Activity'

df = pd.read_sql('TABLE DataFrame;', connStr)

print(df['cadence'])