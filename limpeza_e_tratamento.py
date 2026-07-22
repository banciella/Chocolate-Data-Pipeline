# Importando bibliotecas necessárias
import pandas as pd
import numpy as np

# Lendo o arquivo CSV com os dados de vendas de chocolate
# low_memory=False evita problemas de tipos misturados em colunas grandes
df_choco = pd.read_csv("vendas_chocolate.csv", low_memory = False)

# Exibindo o DataFrame completo
display(df_choco)

# Exibindo a lista de colunas
display(list(df_choco.columns))

# Exibindo informações gerais sobre o DataFrame (tipos, nulos, etc.)
display(df_choco.info())

# Exibindo estatísticas descritivas (média, desvio padrão, etc.)
display(df_choco.describe())

# Substituindo valores nulos por 0 em colunas numéricas específicas
df_choco[["Discount_Pct", "Price_per_Box", "Marketing_Spend"]].fillna(0, inplace=True)

# Conferindo novamente as informações do DataFrame após a limpeza
display(df_choco.info())

# Tentativa de substituir nulos novamente (sem inplace, não altera o DataFrame original)
df_choco[["Discount_Pct","Price_per_Box","Marketing_Spend"]].fillna(0)

# Conferindo novamente as informações
display(df_choco.info())

# Exibindo o DataFrame atualizado
display(df_choco)

# Importando biblioteca para conexão direta com SQL Server
import pyodbc

# Configurações da conexão com SQL Server
server = "localhost\\SQLEXPRESS"   # nome do servidor
database = "Felipe"                # nome do banco de dados
driver = "ODBC Driver 17 for SQL Server"

# Conexão usando autenticação do Windows
conn = pyodbc.connect(
    f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)

# Exemplo de conexão usando usuário/senha (comentado)
# conn = pyodbc.connect(
#     f"DRIVER={driver};SERVER={server};DATABASE={database};UID=seu_usuario;PWD=sua_senha"
# )

# Criando cursor para executar comandos SQL
cursor = conn.cursor()

# Testando conexão com um SELECT simples
cursor.execute("SELECT 1")
print(cursor.fetchone())

# Fechando conexão
conn.close()

# Importando SQLAlchemy para integração com Pandas
from sqlalchemy import create_engine

# Configurações da conexão
server = "localhost\\SQLEXPRESS"
database = "Felipe"
driver = "ODBC Driver 17 for SQL Server"

# String de conexão usando autenticação do Windows
conn_str = f"mssql+pyodbc://@{server}/{database}?driver={driver}"
engine = create_engine(conn_str)

# Exportando o DataFrame para o SQL Server
# Cria a tabela "ChocoVendas" no banco de dados
# if_exists="replace" sobrescreve a tabela caso já exista
# index=False evita criar coluna extra de índice
df_choco.to_sql("ChocoVendas", engine, if_exists="replace", index=False)
