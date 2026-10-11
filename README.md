# Data Engineering Interview Practice

**320 hands-on interview questions** across **SQL (PostgreSQL), Python, Pandas, and PySpark**, with 80 questions per track. Designed for self-study, hands-on data engineering interview preparation, and practicing data quality, transformations, and analytical problem-solving.

## What's included

| Track | Questions | Environment | Focus |
| --- | ---: | --- | --- |
| SQL | 80 | PostgreSQL | Joins, aggregations, CTEs, window functions, analytics, and edge cases |
| Python | 80 | Python 3 | Data processing, validation, transformations, and problem-solving |
| Pandas | 80 | Python + Pandas | DataFrames, grouping, joins, cleaning, and analytics |
| PySpark | 80 | Python + Apache Spark | Distributed DataFrames, transformations, joins, windows, and data quality |
| **Total** | **320** | | |

The Python, Pandas, and PySpark tracks use realistic sample datasets with deliberately messy records to practice handling missing, duplicate, inconsistent, and invalid data. The SQL track uses a locally seeded PostgreSQL database.

## Repository structure

```text
coding-exercises/
├── README.md                     # This guide
├── requirements.txt              # Python dependencies
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

- **Python 3** and `pip` (the project was developed/tested locally with **Python 3.14**).
- **VS Code** with the Python and Jupyter extensions, or another Jupyter notebook environment.
- **Java JDK** compatible with your installed PySpark version for the PySpark track; configure `JAVA_HOME` if needed.
- **PostgreSQL** for the SQL track only (developed/tested locally with **PostgreSQL 18**). No database server is needed for Python, Pandas, or PySpark.

The local PySpark environment used **Spark 4.2.0**. The dependency file does not necessarily pin all versions; if a newer package behaves differently, use compatible versions and consult the relevant project's documentation.


## PySpark / Java Setup

The PySpark exercises require a compatible Java Development Kit (JDK). Installing the Python `pyspark` package alone does not install Java.

### Recommended Environment

| Component | Recommended Version |
|---|---|
| Python | 3.11–3.14 (depending on PySpark compatibility) |
| Apache Spark / PySpark | 4.2.0 (locally tested) |
| Java JDK | 17 or 21 |
| IDE | VS Code with Python and Jupyter extensions |

> **Note:** This project was developed and tested locally using PySpark 4.2.0. Other versions may work, but compatibility is not guaranteed. Spark 4.x requires Java 17 or later. Check the official [Apache Spark documentation](https://spark.apache.org/docs/latest/) for version-specific requirements.

### 1. Install Java JDK

#### macOS (Homebrew)

Install OpenJDK 17:

```bash
brew install openjdk@17
```

Register the JDK with macOS:

```bash
sudo ln -sfn "$(brew --prefix openjdk@17)/libexec/openjdk.jdk" /Library/Java/JavaVirtualMachines/openjdk-17.jdk
```

Configure `JAVA_HOME` for the current terminal session:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
```

To make these settings persistent when using the default macOS Zsh shell:

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

1. Download and install **Eclipse Temurin JDK 17** from [Adoptium](https://adoptium.net/).
2. During installation, enable the options to set `JAVA_HOME` and update `PATH`, if available.
3. Restart VS Code and open a new terminal.

Verify Java in PowerShell:

```powershell
java -version
echo $env:JAVA_HOME
```

If `JAVA_HOME` is missing, configure it through:

**System Properties → Advanced → Environment Variables**

Set `JAVA_HOME` to your JDK installation directory and add `%JAVA_HOME%\bin` to `Path`.

#### Ubuntu / Debian Linux

Install OpenJDK 17:

```bash
sudo apt update
sudo apt install -y openjdk-17-jdk
```

Configure `JAVA_HOME` for the current terminal session:

```bash
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f "$(which java)")")")
export PATH="$JAVA_HOME/bin:$PATH"
```

To make the configuration persistent, add the appropriate `JAVA_HOME` and `PATH` exports to your shell startup file (for example, `~/.bashrc`).

### 2. Verify Java Installation

Open a new terminal and run:

```bash
java -version
```

Expected output should indicate Java 17 or another compatible version.

On macOS / Linux, verify `JAVA_HOME`:

```bash
echo $JAVA_HOME
```

On Windows PowerShell:

```powershell
echo $env:JAVA_HOME
```

### 3. Install Python Dependencies

From the repository root, create and activate a Python virtual environment.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> **Version compatibility:** The `requirements.txt` file does not pin PySpark to a specific version. For the locally tested Spark version, you can explicitly install `pyspark==4.2.0`, provided it is compatible with your Python environment.

### 4. Verify PySpark Installation

Run the following Python code in a notebook or Python script:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("DataEngineeringInterviewPractice")
    .getOrCreate()
)

print("Spark version:", spark.version)

df = spark.createDataFrame(
    [(1, "Alice"), (2, "Bob")],
    ["id", "name"]
)

df.show()

spark.stop()
```

Expected DataFrame output:

```text
+---+-----+
| id| name|
+---+-----+
|  1|Alice|
|  2|  Bob|
+---+-----+
```

If the DataFrame is displayed successfully, your local PySpark environment is ready.

### 5. Common Troubleshooting

| Issue | Possible Solution |
|---|---|
| `JAVA_HOME is not set` | Install a compatible JDK and configure `JAVA_HOME`. |
| `java: command not found` | Verify the Java installation and update `PATH`. |
| `UnsupportedClassVersionError` | Check that your Java version is compatible with your Spark version. |
| `Py4JJavaError` | Inspect the underlying Java exception and verify Java/Spark compatibility. |
| Spark session fails to start | Restart VS Code or the Jupyter kernel after changing Java environment variables. |
| Python / PySpark compatibility error | Verify the supported Python versions for your installed PySpark release. |

> **Important:** These exercises run locally using Spark's local execution mode. A Databricks workspace, Hadoop cluster, or separate Spark cluster is not required.

## Quick start (macOS / Linux)

Open a terminal in the repository root:

```bash
git clone <YOUR_REPOSITORY_URL>
cd data-engineering-interview-practice
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
code .
```

In VS Code, open a notebook and choose the `.venv` Python interpreter/kernel. On Windows, activate the environment with `.venv\Scripts\activate` in Command Prompt or `.venv\Scripts\Activate.ps1` in PowerShell.

**Recommended notebook workflow (Python / Pandas / PySpark):**

1. `01_*dataset_setup.ipynb` — prepare/check sample data.
2. `02_*questions.ipynb` — attempt the 80 exercises yourself.
3. `03_*questions_and_solutions.ipynb` — compare with reference solutions.
4. `04_*validation.ipynb` — run dataset/execution validation.
5. `05_*independent_correctness_audit.ipynb` — run question-specific correctness checks.

The exact `04_` and `05_` filenames vary by track. Keep the `data/` directory alongside the notebooks, as the notebooks may rely on relative paths. Run notebooks from the repository workspace or their track folder as documented within each notebook.

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
6. Run `sql/04_sql_interview_validate_all_80.ipynb` and `sql/05_sql_interview_correctness_tests.ipynb` to check the solutions against your current database.

See [`sql/README.md`](sql/README.md) for details, including working-directory requirements. All five SQL notebooks use `sql/db_connection.py` to read the same local configuration.

## Validation and scope

The project includes executable reference solutions and validation/correctness notebooks. In the author's local test environment, **80/80 questions in each track passed the available execution and correctness checks** (320/320 overall). The Python, Pandas, and PySpark dataset validation checks also passed (45/45 combined).

These results describe the tested datasets, versions, and implemented checks; **they are not a guarantee of correctness for every possible input or environment**. You can rerun the checks after changing a solution or a dataset. SQL checks require the database to be initialized and reachable.

## Keeping a public fork safe

- **Never commit** `sql/db_config.ini`, `.env` files, passwords, tokens, API keys, database dumps, or personal data.
- Keep `.venv/`, notebook checkpoints, local IDE settings, and generated temporary files out of Git.
- Review notebook **code, markdown, and saved cell outputs** for local paths, credentials, or other sensitive information before publishing.
- `.gitignore` does **not** remove secrets already committed to Git history. If a secret was committed, revoke/rotate it and clean the history before making the repository public.
- The provided datasets are intended for practice; inspect any additional datasets before sharing them.

## Contributing and usage

This is a self-study resource. Try each exercise before opening the reference solution; then use the validation notebooks to check your work. Suggestions and improvements can be submitted through GitHub issues or pull requests if those features are enabled on the repository.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
