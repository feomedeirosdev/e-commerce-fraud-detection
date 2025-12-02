# %%
from pathlib import Path
from pandas import read_csv

# %%
transactions_csv_path = Path(__file__).parents[1]/"data"/"transactions.csv"

# %%
df_transactions = read_csv(transactions_csv_path)
df_transactions.info()

# %%
