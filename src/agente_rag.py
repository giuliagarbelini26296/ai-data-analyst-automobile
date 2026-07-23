import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv
import os

load_dotenv()

# Carregar dados limpos
df = pd.read_csv('data/dados_limpos.csv')

# Criar o modelo Groq (gratuito!)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Criar o agente que entende os dados
agente = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True,
    prefix="Você é um analista de dados especialista. Responda as perguntas com base no DataFrame fornecido. "
           "Sempre mostre os números, faça comparações e destaque insights interessantes."
)

# Loop de perguntas
print("🤖 AI Data Analyst pronto! Faça suas perguntas (ou 'sair' para encerrar)\n")
while True:
    pergunta = input("👉 ")
    if pergunta.lower() in ['sair', 'exit', 'quit']:
        break
    resposta = agente.invoke(pergunta)
    print(f"\n📊 {resposta['output']}\n")