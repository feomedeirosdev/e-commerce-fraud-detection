# %%
from pathlib import Path
import pandas as pd

transactions_csv_path = Path(__file__).resolve().parents[2]/'data'/'raw'/'transactions.csv'

df = pd.read_csv(transactions_csv_path)

print(df.info())
print(df.describe())
print(df.describe(exclude=['int', 'float']))
print(df['is_fraud'].value_counts(normalize=True))

# %%
