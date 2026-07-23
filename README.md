# 🏎️ AI Data Analyst — Automobile Market Dataset

Analisador de dados inteligente para o dataset **Automobile Market**, construído com **Python + LangChain + Pandas**. Permite fazer perguntas em linguagem natural sobre os dados e obter respostas com análises estatísticas e insights.

## 📊 Sobre o Dataset

- **Fonte:** Kaggle — Automobile Market Dataset
- **Registros:** 1.329 carros (após limpeza)
- **Colunas:** 18 (Make, Model, Year, Fuel_Type, Transmission, Engine_Size, Mileage, Horsepower, Torque, Owners, Accident_History, Service_History, Color, Body_Type, Drivetrain, Fuel_Efficiency, Location, Selling_Price)

## 🧠 Funcionalidades

- ✅ Responder perguntas em linguagem natural sobre os dados
- ✅ Encontrar o carro mais caro e mais barato
- ✅ Média de preço por fabricante, câmbio e combustível
- ✅ Correlação entre variáveis (ex: Horsepower × Selling_Price)
- ✅ Análise estatística descritiva

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| **Python 3.9+** | Linguagem principal |
| **Pandas** | Manipulação e análise dos dados |
| **LangChain** | Framework de agentes com IA |
| **LangChain Experimental** | Agente Pandas DataFrame |
| **DeepSeek / Gemini** | Modelo de linguagem (IA) |

## 📁 Estrutura do Projeto

ai-data-analyst/
├── data/
│   ├── automobile_dataset.csv      # Dataset original (não versionado)
│   ├── dados_limpos.csv            # Dataset limpo (não versionado)
│   └── .gitkeep
├── src/
│   ├── preparar_dados.py           # Script de limpeza dos dados
│   ├── agente_rag.py               # Agente com IA (via API)
│   └── analisador_local.py         # Analisador local sem API
├── .env                            # Chaves de API (não versionado)
├── .gitignore
├── requirements.txt
└── README.md


## 🚀 Como Usar

### 1. Clonar o repositório
```bash
git clone https://github.com/giuliagarbelini26296/ai-data-analyst-automobile.git
cd ai-data-analyst-automobile

### 2. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

### 3. Instalar dependências
pip install -r requirements.txt

### 4. Colocar o dataset
Baixe o dataset do Kaggle e coloque o arquivo .csv na pasta data/.

### 5. Limpar os dados
python src/preparar_dados.py

### 6. Executar o analisador
Opção A — Analisador local (sem API):python src/analisador_local.py
Opção B — Agente com IA (requer chave de API):Configure a chave no arquivo .env:DEEPSEEK_API_KEY=sua_chave_aqui
Depois execute:python src/agente_rag.py

💬 Exemplos de Perguntas
"Qual o carro mais caro do dataset?"
"Qual a média de preço por fabricante?"
"Carros automáticos são mais caros que manuais?"
"Qual a correlação entre Horsepower e Selling_Price?"
"Quantos carros têm cada tipo de combustível?"

📄 LicençaEste projeto é de código aberto para fins educacionais e de portfólio.

👩‍💻 Autora: Giulia Maria Garbelini Ribeiro
📧 giuliamgrib@gmail.com
🔗 linkedin.com/in/giulia-garbelini
