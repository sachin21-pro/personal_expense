# Personal Expense & Budget Manager

**Project No.:** 28  
**Language:** Python 3  
**Library:** Pandas

## Features
- Set and save a monthly budget in `budget.json`.
- Add expenses with a date, category, and positive amount.
- Store expense records in `expenses.csv` using Pandas.
- Display category-wise totals using `groupby()`.
- Generate a report showing total spent, remaining budget, and percentage used.
- Display a warning when 80% or more of the budget is used.
- Display `Budget exceeded!` when spending is greater than 100% of the budget.
- Validate date format, category, and amount.

## Requirements
- Python 3.9+
- pandas

## Setup
Open a terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
python personal_expense_manager.py
```

## Menu
1. Set Monthly Budget
2. Add Expense
3. Category Summary
4. View Expense Report
5. Exit

## Data files
- `expenses.csv` stores expense records (`Date,Category,Amount`).
- `budget.json` stores the monthly budget.

Both files are included with clean starter data. The program also creates/loads them automatically. Keep them in the same folder as the Python file.

## Note about assignment test cases
The supplied test cases do not specify a report month for every expense. To keep those test cases reproducible, the report and category summary include all valid expense rows currently stored in `expenses.csv`. Start with the included empty CSV when running the test cases. Old entries are not included in this ZIP.

## Date format
Enter dates as `YYYY-MM-DD`, for example `2026-10-05`.
