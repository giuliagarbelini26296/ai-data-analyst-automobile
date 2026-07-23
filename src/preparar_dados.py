import pandas as pd
import os

# Carregar o dataset que você baixou
# (ajusta o nome do arquivo pro que você baixou)
df = pd.read_csv('data/automobile_dataset.csv')

print(f"📊 Base carregada: {len(df)} linhas e {len(df.columns)} colunas")
print(f"📋 Colunas: {list(df.columns)}")
print(f"\n🔍 Amostra:")
print(df.head(3))

# Limpeza básica
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Salvar versão limpa
os.makedirs('data', exist_ok=True)
df.to_csv('data/dados_limpos.csv', index=False)
print(f"\n✅ Dados limpos salvos! {len(df)} registros prontos.")