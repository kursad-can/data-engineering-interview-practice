# Data Engineering Interview Practice

**320 hands-on interview questions** across **SQL (PostgreSQL), Python, Pandas, and PySpark**, with 80 questions per track. Designed for self-study, hands-on data engineering interview preparation, and practicing data quality, transformations, and analytical problem-solving.

Whether you're preparing for your first Data Engineering interview or sharpening your skills for a senior-level role, this repository provides practical exercises covering real-world data engineering concepts.

**Looking for personalized interview preparation?** Check out [Data Role Ready](https://www.dataroleready.com), an AI-powered interview preparation platform that helps you prepare based on your resume and target job description.

## What's included

| Track | Questions | Environment | Focus |
| --- | ---: | --- | --- |
| SQL | 80 | PostgreSQL | Joins, aggregations, CTEs, window functions, analytics, and edge cases |
| Python | 80 | Python 3 | Data processing, validation, transformations, and problem-solving |
| Pandas | 80 | Python + Pandas | DataFrames, grouping, joins, cleaning, and analytics |
| PySpark | 80 | Python + Apache Spark | Distributed DataFrames, transformations, joins, windows, and data quality |
| **Total** | **320** | | |

The Python, Pandas, and PySpark tracks use realistic sample datasets with deliberately messy records to practice handling missing, duplicate, inconsistent, and invalid data. The SQL track uses a locally seeded PostgreSQL database.

### What You'll Practice

- Writing SQL queries for realistic business scenarios.
- Solving Python data processing and transformation problems.
- Cleaning, joining, and analyzing datasets with Pandas.
- Building distributed transformations using PySpark.
- Handling null values, duplicates, invalid records, and edge cases.
- Applying data quality checks and validation techniques.
- Developing the problem-solving skills needed for Data Engineering technical interviews.

**All 320 exercises are available for free in this repository. No Data Role Ready account is required.**

## Repository structure

```text
data-engineering-interview-practice/
├── README.md                     # This guide
├── requirements.txt              # Python dependencies
├── constraints.txt               # Tested shared transitive dependency versions
├── scripts/environment_preflight.py
├── .gitignore                    # Excludes local files and credentials
├── sql/
│   ├── README.md                 # Detailed PostgreSQL setup
│   ├── db_connection.py          # Shared connection helper
│   ├── db_config.example.ini     # Safe configuration template
│   ├── 01_*.ipynb                # PostgreSQL dataset setup (resets tables)
│   ├── 02_*.ipynb                # Questions
│   ├── sql_interview_solutions.ipynb
│   ├── 04_*.ipynb                # Execution validation
│   └── 05_*.ipynb                # Correctness tests
├── python/
│   ├── data/                     # Sample data
│   └── 01_*.ipynb ... 05_*.ipynb
├── pandas/
│   ├── data/
│   └── 01_*.ipynb ... 05_*.ipynb
└── pyspark/
    ├── data/
    └── 01_*.ipynb ... 05_*.ipynb
```

> Notebook filenames may differ slightly between tracks; use the numbered prefixes and descriptive names to identify each step. Local `.venv/`, `.vscode/`, and `sql/db_config.ini` are not meant to be committed.

## Prerequisites

- **CPython 3.11 or 3.12**, with **3.12 recommended**, and `pip`. Use a dedicated virtual environment; the supported baseline does not include Python 3.14.
- **VS Code** with the Python and Jupyter extensions, or another Jupyter notebook environment.
- **Java JDK 17** for the PySpark track. Set `JAVA_HOME` to the JDK directory when Java is not on PATH or multiple Java installations exist. Do not replace system Java.
- **PostgreSQL** for the SQL track only (developed/tested locally with **PostgreSQL 18**). No database server is needed for Python, Pandas, or PySpark.

### Supported environment

| Component | Version |
| --- | --- |
| Python | 3.11.x or 3.12.x (3.12 recommended) |
| Pandas / NumPy | 2.3.3 / 2.2.6 |
| PySpark / PyArrow | 4.2.0 / 19.0.1 |
| Java | JDK 17 |
| PostgreSQL adapter | psycopg2-binary 2.9.10 |
| Jupyter / ipykernel | 1.1.1 / 6.30.1 |

This retains the previously tested Spark version while avoiding the Pandas 3 compatibility warning. [Spark 4.2 requires Python 3.10+, Java 17+, Pandas 2.2–2.x and Arrow 18+ for its Pandas/Arrow integrations](https://spark.apache.org/docs/4.2.0/api/python/getting_started/install.html). [Arrow 19 supports Python 3.11 and 3.12](https://arrow.apache.org/docs/19.0/python/install.html). PyArrow is included so the preflight tests the complete Python/Pandas/Arrow worker path, even though most exercises use native Spark operations.

`requirements.txt` pins direct dependencies and uses `constraints.txt` for the tested shared transitive versions. Constraints do not force installation of another OS's packages; pip resolves additional platform-specific dependencies. This is a version-pinned environment, not a cross-platform artifact/hash lock. Do not independently upgrade packages or mix it with an existing Python 3.14 environment.

## Quick start (macOS / Linux)

Clone the repository, then run the setup commands from its root:

```bash
git clone https://github.com/kursad-can/data-engineering-interview-practice
cd data-engineering-interview-practice
python3.12 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --sys-prefix --name de-practice --display-name "DE Practice (Python 3.12)"
python scripts/environment_preflight.py
code .
```

Use an unused environment directory: do not overwrite an existing `venv/` or `.venv/`. Substitute `python3.11` and the matching kernel display name if using Python 3.11. These commands install only into the new venv; they do not change the system interpreter. Notebook initialization no longer runs package installers.

In VS Code's notebook kernel picker, select **DE Practice (Python 3.12)** or the new `venv` interpreter, not an old saved `.venv (3.14.2)` label. In Jupyter, launch `python -m jupyter lab` from the activated environment and select the same kernel. Restart a notebook kernel after changing its environment. The kernel registration above is stored inside the venv, not in system directories.

### Windows and platform notes

In PowerShell, use `py -3.12 -m venv venv`, then `venv\Scripts\Activate.ps1`; run the same `python -m pip`, kernel-registration and preflight commands above. In Command Prompt, activation is `venv\Scripts\activate.bat`. If PowerShell blocks activation, use `venv\Scripts\python.exe` explicitly rather than changing a machine-wide execution policy.

- **macOS Apple Silicon:** use native ARM64 Python and JDK 17 consistently, not a mixture of Rosetta and native runtimes. If JDK 17 is already registered, select it for the current shell with `export JAVA_HOME=$(/usr/libexec/java_home -v 17)`.
- **Linux:** Python's `venv` support must be available. Select an existing JDK 17 through `JAVA_HOME`; its value is the JDK root, not its `bin` directory.
- **Windows:** use matching 64-bit Python/JDK installations and set `JAVA_HOME` for the current shell to the installed JDK 17 directory. Allow local Java/Python communication if prompted by the firewall. If native Spark/Hadoop initialization is unavailable on a particular Windows installation, use WSL2 with a separate Linux venv/JDK; do not download unofficial Hadoop executables as a workaround.
- Fresh isolated environments with Python 3.12.8 and 3.11.8 were tested on macOS Apple Silicon: both passed preflight, all 320 correctness checks and all 45 lightweight checks. Windows and Linux are supported version targets, not claims of platform-specific test runs. PostgreSQL server setup is separate; the SQL audit was exercised against PostgreSQL 18.1 without reseeding.

### Installing JDK 17 if needed

The Python `pyspark` package does not install Java. If JDK 17 is already available, select it as described above; do not replace system Java. Otherwise, install a separate JDK 17:

- **macOS (Homebrew):** `brew install openjdk@17`. Select that installation for the current shell with `export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"` and `export PATH="$JAVA_HOME/bin:$PATH"`. This avoids changing the system JDK registration.
- **Windows:** obtain Eclipse Temurin JDK 17 from [Adoptium](https://adoptium.net/). Set `JAVA_HOME` to its installation directory and add its `bin` directory to the current shell's `PATH`; restart the notebook kernel after changing the environment.
- **Ubuntu / Debian:** if you administer the machine, install `openjdk-17-jdk` with your package manager (`sudo apt update`, then `sudo apt install openjdk-17-jdk`). Select its JDK root through `JAVA_HOME` without replacing another application's Java configuration.

Run `java -version` and verify that the selected version is 17. Inspect `echo "$JAVA_HOME"` on macOS/Linux or `echo $env:JAVA_HOME` in PowerShell. Add shell settings to your own startup file only if you want them to persist. No Databricks workspace, Hadoop cluster, or separate Spark cluster is required for these local exercises.

### Environment preflight and Spark troubleshooting

From the repository root, run `python scripts/environment_preflight.py` in the activated venv. It checks the interpreter, pinned direct-package versions and imports, Java 17, Spark startup, two Python worker tasks, and an eight-row distributed Pandas UDF/Arrow calculation. It does not read or write exercise datasets, change installations, or require a cloud service. A failed check exits with a nonzero status and troubleshooting guidance.

All Spark notebook initialization cells set both `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` to `sys.executable` **before** session creation, and set the matching `spark.pyspark.python` / `spark.pyspark.driver.python` properties. Local practice uses `local[2]`, retaining distributed execution with modest resource use. This configuration is for local notebooks; a remote cluster needs the same environment deployed on every worker, not the driver's local filesystem path.

If you see `PYTHON_VERSION_MISMATCH`, confirm `sys.executable` points to the new venv, select the correct kernel, restart it completely, and rerun initialization before other cells. Changing environment variables after a SparkContext exists does not rebuild its workers. For gateway/Java errors, check `JAVA_HOME`, `java -version`, and local firewall/hostname settings. Remove stale `SPARK_HOME` or `PYTHONPATH` overrides from the current shell when using pip-installed Spark. Run `python -m pip check` for dependency conflicts; reinstall the pinned requirements inside the dedicated venv rather than upgrading global packages.

### Recommended notebook workflow (Python / Pandas / PySpark)

1. `01_*dataset_setup.ipynb` — load/check the bundled input fixtures without modifying them. Missing files produce an error; setup does not regenerate data.
2. `02_*questions.ipynb` — run its initialization cells, then write each answer in the code cell below the question. Keep solution and audit notebooks closed while attempting an exercise; both contain answers.
3. `03_*questions_and_solutions.ipynb` — after your attempt, run the corresponding reference solution and compare results using the same inputs.
4. `04_*validation.ipynb` — check dataset consistency, presence of all reference solutions, and their Python syntax. These checks do not execute or grade learner answers; they can also be run before practice as a readiness check.
5. `05_*independent_correctness_audit.ipynb` — execute embedded reference implementations against independent checks, not code from your question notebook.

The exact `04_` and `05_` filenames vary by track. Keep the `data/` directory alongside the notebooks. For Python, Pandas and PySpark, start the notebook kernel with its technology directory as the working directory (for example, `cd pyspark` before launching Jupyter); the repository root is not a supported data-loading directory for those tracks. Run each notebook's own initialization cells in a fresh kernel: variables do not carry between notebooks. SQL supports either the repository root or `sql/` as described below.

## SQL: one configuration file for all notebooks

SQL notebooks connect to **your own local PostgreSQL instance**. Connection details are **not** hardcoded into individual notebooks.

1. Install and start PostgreSQL, then create a database (default name: `sql_interview`). For example, with PostgreSQL tools installed:

   ```bash
   createdb sql_interview
   ```

2. From the repository root, create your private connection file:

   ```bash
   cp sql/db_config.example.ini sql/db_config.ini
   ```

3. Edit **`sql/db_config.ini`** with your own settings:

   ```ini
   [postgresql]
   host = localhost
   port = 5432
   dbname = sql_interview
   user = YOUR_POSTGRES_USER
   password =
   ```

   Supply a password only if your PostgreSQL authentication requires one. Do **not** commit `db_config.ini`.

4. Open `sql/01_sql_interview_realistic_reseed_80_coverage.ipynb` and run it **only if you want to initialize/reset the interview tables**. **Warning: the setup notebook recreates its interview tables and can delete existing data in those tables. Use a dedicated practice database.**
5. Work through `sql/02_sql_interview_questions.ipynb`, then compare answers in `sql/sql_interview_solutions.ipynb`.
6. Run `sql/04_sql_interview_validate_all_80.ipynb` for embedded reference-query execution checks, then `sql/05_sql_interview_correctness_tests.ipynb` for independent invariants against your current database. Neither notebook reads your answers from the question notebook.

See [`sql/README.md`](sql/README.md) for details, including working-directory requirements. All five SQL notebooks use `sql/db_connection.py` to read the same local configuration.

## Validation and scope

The project includes executable reference solutions and validation/correctness notebooks. In the author's local test environment, **80/80 questions in each track passed the available execution and correctness checks** (320/320 overall). The Python, Pandas, and PySpark dataset validation checks also passed (45/45 combined).

These results describe the tested datasets, versions, and implemented checks; **they are not a guarantee of correctness for every possible input or environment**. SQL checks require the database to be initialized and reachable. Some SQL checks establish invariants rather than complete output equality.

**The validation notebooks do not automatically grade learner answers.** The `05_` notebooks contain embedded reference implementations; editing a question answer or a separate solution notebook does not automatically replace those embedded copies. The non-SQL `04_` checks inspect solution presence/syntax and datasets; SQL `04_` executes its embedded reference queries. Review the final PASS/FAIL/ERROR totals and details, not just whether Run All finished: some correctness notebooks record failures without raising a final exception.

To check your work manually, run your answer in the question notebook and the corresponding reference in a separate, freshly initialized solution kernel. Compare the full result, not only the displayed preview: values, columns/keys, types where required, row counts, duplicate multiplicities and missing-value behavior. Compare ordering only where the approved question requires it; otherwise compare records without imposing a new sort rule. Equivalent implementations need not use the same methods as the reference. For file-writing exercises, compare the produced files and their contents.

Python Q32 writes `python/data/completed_orders_output.csv`; Q39 writes one `python/data/orders_YYYY-MM-DD.json` per order date. Their audit checks read those outputs after generating them in the same exercise. These are reproducible outputs, not required input fixtures. Running the Python solution/audit notebooks may overwrite them. Validation also writes report CSVs in the current track directory (or repository root for SQL); these reports are ignored by Git. Use an isolated copy of the track when you want to run reference audits without changing your local exercise outputs.

## 🚀 Take Your Data Engineering Interview Preparation Further

### From Coding Practice to Interview Readiness

This repository helps you strengthen your technical skills through **320 free coding exercises**.

However, preparing for a Data Engineering interview often involves more than writing SQL queries or PySpark transformations.

You may also need to:

- Explain your experience with real-world data pipelines and architectures.
- Discuss data engineering design decisions and trade-offs.
- Answer technical and behavioral interview questions.
- Prepare for questions tailored to a specific job description.
- Practice communicating your solutions clearly under interview conditions.

That's why I built **[Data Role Ready](https://www.dataroleready.com)**.

### Meet Data Role Ready

**Data Role Ready** is an AI-powered interview preparation platform designed to help job seekers prepare for the roles they're targeting.

Instead of relying entirely on generic interview questions, Data Role Ready focuses on personalized preparation based on your background and the requirements of the position.

**Key features include:**

- **Resume and Job Description Analysis** — Generate interview preparation tailored to your experience and the role you're applying for.
- **Personalized Interview Questions** — Practice questions relevant to your target position.
- **AI-Powered Mock Interviews** — Simulate interview scenarios and practice your responses.
- **Coding Interview Preparation** — Strengthen technical problem-solving skills.
- **Interview Readiness Assessments** — Identify strengths and areas where additional preparation may help.

### How They Work Together

| This GitHub Repository | Data Role Ready |
|---|---|
| 320 free coding exercises | Personalized interview preparation |
| SQL, Python, Pandas, and PySpark | Preparation based on resumes and job descriptions |
| Hands-on technical practice | AI-powered mock interviews |
| Reference solutions and correctness checks | Interview readiness assessments |
| Self-paced coding practice | Role-specific interview preparation |

**Use this repository to practice your coding skills. Use Data Role Ready to prepare for the interview itself.**

### Ready to Prepare for Your Next Interview?

**👉 [Explore Data Role Ready — AI-Powered Interview Preparation](https://www.dataroleready.com)**

*Data Role Ready is developed by the creator of this repository. The 320 exercises here remain freely available without registration or a paid subscription.*

## Keeping a public fork safe

- **Never commit** `sql/db_config.ini`, `.env` files, passwords, tokens, API keys, database dumps, or personal data.
- Keep `.venv/`, notebook checkpoints, local IDE settings, and generated temporary files out of Git.
- Review notebook **code, markdown, and saved cell outputs** for local paths, credentials, or other sensitive information before publishing.
- `.gitignore` does **not** remove secrets already committed to Git history. If a secret was committed, revoke/rotate it and clean the history before making the repository public.
- The provided datasets are intended for practice; inspect any additional datasets before sharing them.

## Contributing and Usage

This is a free, self-study resource for anyone preparing for Data Engineering interviews.

Try each exercise before opening the reference solution. Then compare your approach with the provided implementation and use the validation notebooks to understand the expected behavior.

Suggestions, corrections, and improvements are welcome through GitHub issues or pull requests if those features are enabled on the repository.

If you find this repository helpful, consider giving it a **GitHub star ⭐** to help other Data Engineering candidates discover it.

For more personalized interview preparation, visit **[Data Role Ready](https://www.dataroleready.com)**.

These validation notebooks check supplied references and datasets, not answers entered in question notebooks. Compare your results manually as described above.

## License

This project is licensed under the MIT License. Retain the copyright and permission notice when redistributing copies or substantial portions; the software is provided without warranty. See the [LICENSE](LICENSE) file for the complete terms.
