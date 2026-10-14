# SQL Interview Practice — PostgreSQL 18

All **five notebooks** share one connection configuration. You never need to edit credentials inside notebooks.

## One-time setup

1. Install and start PostgreSQL; create a database named `sql_interview` (or choose another database name).
2. From the `sql/` folder, copy the sample configuration:

   ```bash
   cp db_config.example.ini db_config.ini
   ```

3. Edit `db_config.ini` in the current `sql/` folder and set `host`, `port`, `dbname`, `user`, and (if required) `password`.
4. Follow the [root environment instructions](../README.md#prerequisites): Python 3.12 is recommended (3.11 is also supported). Install the root `requirements.txt`, which applies `constraints.txt`, inside the dedicated virtual environment; do not install separate unpinned package versions.
5. Open VS Code in the repository root **or** its `sql/` folder, select the practice virtual-environment kernel, and run the initialization cells in each notebook. Kernel state is not shared between notebooks.

**Security:** `db_config.ini` is excluded by the repository's root [`.gitignore`](../.gitignore); there is no separate `sql/.gitignore`. Commit only `db_config.example.ini`. Never put real credentials in notebooks or screenshots. Ignore rules do not protect files already tracked in Git; review tracking before publishing.

**Passwordless connections:** Leave `password =` blank when your local PostgreSQL uses trust/peer authentication or libpq's `.pgpass`/environment mechanisms.

## Recommended order

- `01_sql_interview_realistic_reseed_80_coverage.ipynb` — **destructive**: recreates the interview tables. Run only when you want to reset data.
- `02_sql_interview_questions.ipynb` — solve 80 questions yourself in the provided SQL answer cells; keep solutions and audits closed while practicing.
- `sql_interview_solutions.ipynb` — run a reference solution after your attempt and manually compare full results on the same database. Preserve duplicate rows, NULL semantics and ordering only as specified by the question.
- `04_sql_interview_validate_all_80.ipynb` — executes embedded reference queries and checks execution/data coverage, not learner answers.
- `05_sql_interview_correctness_tests.ipynb` — runs embedded reference queries with independent invariants and fixture-coverage checks. Some invariants are weaker than full result comparisons; inspect every final status and detail.

Neither validation notebook automatically reads code from your question or solution notebook. Editing those notebooks does not update the embedded reference copies. Passing the audits therefore does not certify a learner's answer.

`sql_interview_validation_report.csv` and `sql_interview_correctness_report.csv` are written to the current working directory. The root `.gitignore` excludes both filenames at the repository root and inside `sql/`. The repository contains seed code, not a PostgreSQL database; use the seed notebook to initialize a dedicated practice database. It recreates the interview tables after confirmation, so do not run it against valuable tables.

## Working directory

The connection bootstrap locates `db_connection.py` when the Jupyter working directory is either the repository root (`data-engineering-interview-practice/` after cloning) or its `sql/` subdirectory. Open one of those locations as your workspace and verify the kernel's working directory. Unlike SQL, the Python, Pandas and PySpark tracks require their respective track directory as the kernel working directory.
