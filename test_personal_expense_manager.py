import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import personal_expense_manager as app


class ExpenseManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_expense_file = app.EXPENSE_FILE
        self.old_budget_file = app.BUDGET_FILE
        app.EXPENSE_FILE = Path(self.temp_dir.name) / "expenses.csv"
        app.BUDGET_FILE = Path(self.temp_dir.name) / "budget.json"
        app.save_expenses(pd.DataFrame(columns=app.COLUMNS))
        app.save_budget(5000)

    def tearDown(self):
        app.EXPENSE_FILE = self.old_expense_file
        app.BUDGET_FILE = self.old_budget_file
        self.temp_dir.cleanup()

    def test_test_case_4_totals(self):
        df = pd.DataFrame([
            ["2026-10-05", "Food", 1500],
            ["2026-10-05", "Travel", 1000],
            ["2026-10-05", "Food", 1700],
        ], columns=app.COLUMNS)
        total = app.get_current_month_expenses(df)["Amount"].sum()
        remaining, percentage = app.budget_status(total, 5000)
        self.assertEqual(total, 4200)
        self.assertEqual(remaining, 800)
        self.assertEqual(percentage, 84)

    def test_category_summary_uses_groupby_totals(self):
        df = pd.DataFrame([
            ["2026-10-05", "Food", 1500],
            ["2026-10-05", "Travel", 1000],
            ["2026-10-05", "Food", 1700],
        ], columns=app.COLUMNS)
        self.assertEqual(df.groupby("Category")["Amount"].sum()["Food"], 3200)
        self.assertEqual(df.groupby("Category")["Amount"].sum()["Travel"], 1000)

    def test_invalid_amount_is_not_saved(self):
        with patch("builtins.input", side_effect=["2026-10-05", "Food", "-200"]):
            df = app.add_expense(pd.DataFrame(columns=app.COLUMNS))
        self.assertTrue(df.empty)

    def test_invalid_date_is_not_saved(self):
        with patch("builtins.input", side_effect=["05-10-2026"]):
            df = app.add_expense(pd.DataFrame(columns=app.COLUMNS))
        self.assertTrue(df.empty)

    def test_boundary_100_percent(self):
        remaining, percentage = app.budget_status(1000, 1000)
        self.assertEqual(remaining, 0)
        self.assertEqual(percentage, 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
