import pandas as pd

# Carregar dados
df = pd.read_csv('data/dados_limpos.csv')

print("🤖 AI Data Analyst (modo local) pronto!")
print(f"📊 {len(df)} registros, {len(df.columns)} colunas\n")

while True:
    pergunta = input("👉 ").lower()
    
    if pergunta in ['sair', 'exit', 'quit']:
        break
    
    # Análises pré-programadas
    if "mais caro" in pergunta:
        carro = df.loc[df['Selling_Price'].idxmax()]
        print(f"\n🚗 Carro mais caro: {carro['Make']} {carro['Model']} ({carro['Year']})")
        print(f"💰 Preço: ${carro['Selling_Price']:,.0f}")
        print(f"⚡ Motor: {carro['Engine_Size']}L, {carro['Horsepower']} HP")
        print(f"📏 Km: {carro['Mileage']:,} milhas")
        print(f"📍 Local: {carro['Location']}\n")
    
    elif "mais barato" in pergunta:
        carro = df.loc[df['Selling_Price'].idxmin()]
        print(f"\n🚗 Carro mais barato: {carro['Make']} {carro['Model']} ({carro['Year']})")
        print(f"💰 Preço: ${carro['Selling_Price']:,.0f}\n")
    
    elif "média" in pergunta and ("preço" in pergunta or "preco" in pergunta):
        print(f"\n💰 Preço médio geral: ${df['Selling_Price'].mean():,.0f}\n")
    
    elif "média" in pergunta and ("marca" in pergunta or "fabricante" in pergunta):
        print("\n💰 Preço médio por fabricante:")
        print(df.groupby('Make')['Selling_Price'].mean().sort_values(ascending=False).to_string())
        print()
    
    elif "automático" in pergunta or "automatico" in pergunta or "manual" in pergunta:
        print("\n💰 Preço médio por tipo de câmbio:")
        print(df.groupby('Transmission')['Selling_Price'].mean().to_string())
        print()
    
    elif "combustível" in pergunta or "combustivel" in pergunta or "fuel" in pergunta:
        print("\n⛽ Quantidade por tipo de combustível:")
        print(df['Fuel_Type'].value_counts().to_string())
        print()
    
    elif "mais vendido" in pergunta or "top" in pergunta:
        print("\n🏆 Fabricantes com mais carros no dataset:")
        print(df['Make'].value_counts().head(10).to_string())
        print()
    
    elif "correlação" in pergunta or "correlacao" in pergunta:
        print("\n📊 Correlação com o preço de venda:")
        cols_numericas = df.select_dtypes(include='number').columns
        correlacoes = df[cols_numericas].corr()['Selling_Price'].sort_values(ascending=False)
        print(correlacoes.to_string())
        print()
    
    elif "todos" in pergunta or "listar" in pergunta or "lista" in pergunta:
        print("\n📋 Primeiros 10 registros:")
        print(df[['Make', 'Model', 'Year', 'Selling_Price']].head(10).to_string())
        print()

    elif "horsepower" in pergunta or "potência" in pergunta or "potencia" in pergunta or "cavalo" in pergunta or "relação" in pergunta:
        print("\n📊 Relação entre Horsepower e Selling_Price:")
        correlacao = df['Horsepower'].corr(df['Selling_Price'])
        print(f"Correlação de Pearson: {correlacao:.3f}")
        if correlacao > 0.5:
            print("✅ Correlação positiva forte — carros com mais potência tendem a ser mais caros.")
        elif correlacao > 0.3:
            print("📈 Correlação positiva moderada — há alguma relação entre potência e preço.")
        elif correlacao > -0.3:
            print("🔍 Correlação fraca — potência não é um bom preditor isolado de preço.")
        else:
            print("📉 Correlação negativa — carros com mais potência tendem a ser mais baratos.")
            print()
    
    else:
        print("\n❓ Perguntas que posso responder:")
        print("- 'Qual o carro mais caro?'")
        print("- 'Qual o carro mais barato?'")
        print("- 'Qual a média de preço?'")
        print("- 'Média de preço por fabricante?'")
        print("- 'Carros automáticos vs manuais?'")
        print("- 'Tipos de combustível?'")
        print("- 'Top fabricantes?'")
        print("- 'Correlação com preço?'")
        print("- 'Listar todos os carros?'")
        print("- Digite 'sair' para encerrar\n")