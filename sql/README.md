# SQL Interview Practice — PostgreSQL 18

All **five notebooks** share one connection configuration. You never need to edit credentials inside notebooks.

## One-time setup

1. Install and start PostgreSQL; create a database named `sql_interview` (or choose another database name).
2. From the `sql/` folder, copy the sample configuration:

   ```bash
   cp db_config.example.ini db_config.ini
   ```

3. Open `sql/db_config.ini` and set `host`, `port`, `dbname`, `user`, and (if required) `password`.
4. Use the project's Python environment and install `psycopg2-binary`, `pandas`, `ipython`, and `ipykernel` if not installed.
5. Open VS Code in `coding-exercises/` **or** `coding-exercises/sql/`, select the Python kernel, and run notebooks.

**Security:** `db_config.ini` is excluded by `sql/.gitignore`; commit only `db_config.example.ini`. Never put real credentials in notebooks or screenshots. If your repository already tracks `db_config.ini`, untrack it with `git rm --cached sql/db_config.ini`.

**Passwordless connections:** Leave `password =` blank when your local PostgreSQL uses trust/peer authentication or libpq's `.pgpass`/environment mechanisms.

## Recommended order

- `01_sql_interview_realistic_reseed_80_coverage.ipynb` — **destructive**: recreates the interview tables. Run only when you want to reset data.
- `02_sql_interview_questions.ipynb` — solve 80 questions yourself.
- `sql_interview_solutions.ipynb` — reference solutions.
- `04_sql_interview_validate_all_80.ipynb` — execution validation.
- `05_sql_interview_correctness_tests.ipynb` — correctness/invariant checks.

The two report CSVs are generated locally and ignored by Git. Database tables are **not** included in this ZIP; use the seed notebook to populate your own PostgreSQL database.

## Working directory

The connection bootstrap locates `db_connection.py` when the Jupyter working directory is either `coding-exercises/` or `coding-exercises/sql/`. If you open VS Code from elsewhere, open one of those folders as your workspace first.
