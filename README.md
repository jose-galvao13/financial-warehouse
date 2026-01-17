# 🗄️ Financial Data Warehouse

### 📋 Overview
A complete **Data Engineering solution** designed to centralize financial data into a robust SQL architecture.
Moving away from decentralized Excel files, this project builds a **Kimball Star Schema** Data Warehouse from scratch. It simulates an enterprise environment where raw ERP data is extracted, transformed via Python, and loaded into a Relational Database to feed Power BI dashboards.

### 🚀 Key Features
*   **Advanced Data Modeling:** Implementation of a **Star Schema** architecture, separating data into **Fact Tables** (General Ledger Transactions) and **Dimension Tables** (Chart of Accounts, Departments, Time).
*   **Python ETL Pipeline:** Object-Oriented Python script (`Class FinancialETL`) that automates the extraction of raw CSVs, cleans data inconsistencies, and loads it into SQLite.
*   **Automated Date Dimension:** Algorithmic generation of a comprehensive Time Dimension (Year, Quarter, Month) to enable precise time-series analysis in BI tools.
*   **SQL Analytics:** Pre-built SQL Views and complex queries to generate **Profit & Loss (P&L)** statements and Departmental Cost Analysis directly within the database.
*   **Power BI Integration:** Direct connection between Power BI and the SQL Database (via Python script), eliminating manual data refresh processes.

### 🛠️ Tech Stack
*   **Core:** Python 3.10+ & SQL
*   **Database:** SQLite (Relational DB)
*   **Data Processing:** Pandas, NumPy
*   **Visualization:** Microsoft Power BI
*   **IDE Tools:** VS Code, SQLTools
