# %%
from pathlib import Path
import sqlite3
import pandas as pd

root = Path(__file__).resolve()
print(root)

# %%
def create_connection(db_path: Path):
    conn = sqlite3.connect(db_path)
    return conn

def load_csv(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df

def write_table(df: pd.DataFrame, table_name: str, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Tabela {table_name} criada/atualizada com sucesso.")

def main():
    # Caminhos
    root = Path(__file__).resolve().parents[2]