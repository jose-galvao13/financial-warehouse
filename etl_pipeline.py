import sqlite3
import pandas as pd
from datetime import date

DB_NAME = "Financial_Warehouse.db"

class FinancialETL:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print(f"🔌 Conectado à Base de Dados: {db_name}")

    def create_schema(self):
        """Cria o Star Schema (Factos e Dimensões)"""
        print("🏗️ A construir o esquema da base de dados...")
        
        # 1. Dimensão Contas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dim_Account (
                AccountID INTEGER PRIMARY KEY,
                AccountName TEXT,
                Type TEXT,
                Category TEXT
            )
        ''')

        # 2. Dimensão Departamento
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dim_Department (
                DeptID TEXT PRIMARY KEY,
                DeptName TEXT
            )
        ''')

        # 3. Dimensão Tempo (Essencial para BI Profissional)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dim_Date (
                DateKey TEXT PRIMARY KEY,
                Year INTEGER,
                Month INTEGER,
                MonthName TEXT,
                Quarter TEXT
            )
        ''')

        # 4. Tabela de Factos (Onde tudo se liga)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Fact_Ledger (
                TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                DateKey TEXT,
                AccountID INTEGER,
                DeptID TEXT,
                Amount REAL,
                FOREIGN KEY(DateKey) REFERENCES Dim_Date(DateKey),
                FOREIGN KEY(AccountID) REFERENCES Dim_Account(AccountID),
                FOREIGN KEY(DeptID) REFERENCES Dim_Department(DeptID)
            )
        ''')
        self.conn.commit()

    def populate_date_dimension(self, start='2024-01-01', end='2025-12-31'):
        """Gera o calendário automaticamente no SQL"""
        print("📅 A popular a Dimensão Tempo...")
        dates = pd.date_range(start, end)
        date_df = pd.DataFrame({'DateKey': dates})
        date_df['DateKey'] = date_df['DateKey'].dt.strftime('%Y-%m-%d')
        date_df['Year'] = dates.year
        date_df['Month'] = dates.month
        date_df['MonthName'] = dates.strftime('%B')
        date_df['Quarter'] = 'Q' + dates.quarter.astype(str)
        
        date_df.to_sql('Dim_Date', self.conn, if_exists='replace', index=False)

    def run_etl_process(self):
        """Extrai CSVs, Transforma e Carrega no SQL"""
        print("🚀 A iniciar processo ETL...")

        # A. Carregar Dimensões (Full Refresh)
        df_acc = pd.read_csv('source_accounts.csv')
        df_acc.to_sql('Dim_Account', self.conn, if_exists='replace', index=False)
        print(f"   -> {len(df_acc)} Contas carregadas.")

        df_dept = pd.read_csv('source_departments.csv')
        df_dept.to_sql('Dim_Department', self.conn, if_exists='replace', index=False)
        print(f"   -> {len(df_dept)} Departamentos carregados.")

        # B. Carregar Factos (Ledger)
        df_ledger = pd.read_csv('source_ledger.csv')
        
        # Transformação: Garantir que a data é string limpa para ligar à Dim_Date
        df_ledger['DateKey'] = pd.to_datetime(df_ledger['Date']).dt.strftime('%Y-%m-%d')
        
        # Selecionar apenas as colunas que correspondem à tabela SQL (mapeamento)
        fact_table = df_ledger[['DateKey', 'AccountID', 'DeptID', 'Amount']]
        
        # Append (Adicionar ao histórico existente)
        fact_table.to_sql('Fact_Ledger', self.conn, if_exists='append', index=False)
        print(f"   -> {len(fact_table)} Transações processadas e inseridas.")

    def close(self):
        self.conn.close()
        print("🏁 Conexão fechada. Warehouse atualizado.")

if __name__ == "__main__":
    etl = FinancialETL(DB_NAME)
    etl.create_schema()
    etl.populate_date_dimension()
    etl.run_etl_process()