# %%
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

db_path = Path(__file__).parents[1]/"data"/"transactions.csv"

df = pd.read_csv(db_path)

print(df.info())

print(df['is_fraud'].value_counts(normalize=True))

# %%
fraud_counts = df['is_fraud'].value_counts(normalize=True)

# %%
plt.rcParams['figure.figsize'] = (4, 3)
plt.bar(fraud_counts.index, fraud_counts.values)
plt.xticks([0,1], ['Legítima', 'Fraude'])
plt.ylabel('nº de transações')
plt.savefig("../img/hist_amount.jpg", dpi=150, format="jpg")

plt.close()

# %%
print(fraud_counts)

# %%
print(f'Legítimas: {fraud_counts[0]*100:.2f} %')
print(f'Fraudes:   {fraud_counts[1]*100:.2f} %')

# %%
df.info()

# %%
# Histograma de amounts
plt.hist(df['amount'], bins=50, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Valor da transação')
plt.ylabel('Número de transações')
# plt.title('Distribuição de valores transacionais')
plt.yscale('log')  # escala log para visualizar melhor as caudas
plt.show()

# %%
country_counts = df.groupby('bin_country')['is_fraud'].sum().sort_values(ascending=False)
total_counts = df['bin_country'].value_counts()

# Fraudes relativas
fraud_ratio = (country_counts / total_counts).sort_values(ascending=False)

fraud_ratio.plot(kind='bar', color='orange')
plt.ylabel('Proporção de fraudes')
plt.title(f'Proporção de fraudes por país (bin_country)')
plt.show()

# %%
plt.scatter(df['account_age_days'], df['is_fraud'], alpha=0.01, color='purple')
plt.xlabel('Dias de existência da conta')
plt.ylabel('Fraude (0/1)')
plt.title('Fraude vs Idade da conta')
plt.show()


# %%
plt.boxplot([df[df['is_fraud']==0]['shipping_distance_km'],
             df[df['is_fraud']==1]['shipping_distance_km']],
            labels=['Legítima', 'Fraude'])
plt.yscale('log')
plt.ylabel('Distância de envio (km)')
plt.title('Distribuição de distância de envio por classe')
plt.show()

# %%
