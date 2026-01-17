SELECT 
    d.Year,
    d.Quarter,
    a.Category,
    SUM(f.Amount) as Total_Amount
FROM Fact_Ledger f
JOIN Dim_Date d ON f.DateKey = d.DateKey
JOIN Dim_Account a ON f.AccountID = a.AccountID
WHERE a.Type IN ('Revenue', 'Expense')
GROUP BY d.Year, d.Quarter, a.Category
ORDER BY d.Year, d.Quarter, a.Category;

SELECT 
    dept.DeptName,
    SUM(f.Amount) as Total_Cost
FROM Fact_Ledger f
JOIN Dim_Department dept ON f.DeptID = dept.DeptID
JOIN Dim_Account a ON f.AccountID = a.AccountID
WHERE a.Type = 'Expense' -- Apenas gastos
GROUP BY dept.DeptName
ORDER BY Total_Cost ASC; -- Como são negativos, o menor número é o maior gasto

CREATE VIEW View_Financial_Report AS
SELECT 
    f.TransactionID,
    d.DateKey,
    d.MonthName,
    d.Year,
    a.AccountName,
    a.Type as AccountType,
    dept.DeptName,
    f.Amount
FROM Fact_Ledger f
LEFT JOIN Dim_Date d ON f.DateKey = d.DateKey
LEFT JOIN Dim_Account a ON f.AccountID = a.AccountID
LEFT JOIN Dim_Department dept ON f.DeptID = dept.DeptID;

