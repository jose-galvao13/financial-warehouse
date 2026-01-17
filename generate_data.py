import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Gerar Dimensão: Plano de Contas (Chart of Accounts)
# Estrutura hierárquica complexa
accounts_data = {
    'AccountID': [4010, 4020, 5010, 5020, 6210, 6220, 1010, 2010],
    'AccountName': ['Sales Revenue', 'Service Revenue', 'COGS', 'Staff Costs', 'Marketing', 'IT Expenses', 'Cash', 'Payables'],
    'Type': ['Revenue', 'Revenue', 'Expense', 'Expense', 'Expense', 'Expense', 'Asset', 'Liability'],
    'Category': ['Sales', 'Sales', 'Direct Costs', 'OpEx', 'OpEx', 'OpEx', 'Treasury', 'Current Liab']
}
df_accounts = pd.DataFrame(accounts_data)

# 2. Gerar Dimensão: Centros de Custo (Cost Centers)
departments_data = {
    'DeptID': ['D01', 'D02', 'D03', 'D99'],
    'DeptName': ['Sales Dept', 'IT Dept', 'HR Dept', 'General']
}
df_depts = pd.DataFrame(departments_data)

# 3. Gerar Factos: 10.000 Transações (General Ledger)
print("A gerar 10.000 transações financeiras...")
dates = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(365)]

transactions = []
for _ in range(10000):
    date = np.random.choice(dates)
    acct = np.random.choice(df_accounts['AccountID'])
    dept = np.random.choice(df_depts['DeptID'])
    
    # Lógica simples: Vendas são positivas, Gastos negativos (para simplificar)
    base_amount = np.random.uniform(100, 5000)
    amount = base_amount if acct < 5000 else -base_amount
    
    transactions.append([date, acct, dept, round(amount, 2)])

df_ledger = pd.DataFrame(transactions, columns=['Date', 'AccountID', 'DeptID', 'Amount'])

# Exportar para CSV (Simulando a exportação do ERP)
df_accounts.to_csv('source_accounts.csv', index=False)
df_depts.to_csv('source_departments.csv', index=False)
df_ledger.to_csv('source_ledger.csv', index=False)

print("✅ Dados brutos gerados: source_accounts.csv, source_departments.csv, source_ledger.csv")