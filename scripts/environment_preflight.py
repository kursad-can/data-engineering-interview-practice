"""Read-only local environment smoke test; run with the practice venv's Python."""

import importlib
import importlib.metadata
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


def check_packages():
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    if sys.version_info[:2] not in {(3, 11), (3, 12)}:
        raise RuntimeError("Use Python 3.11 or 3.12 to create a new practice venv; do not replace system Python.")
    if sys.prefix == sys.base_prefix:
        raise RuntimeError("Activate the dedicated virtual environment before running this check.")
    requirements = Path(__file__).resolve().parents[1] / "requirements.txt"
    for line in requirements.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith(("#", "-c ")):
            continue
        package, expected = line.split("==")
        try:
            actual = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError as exc:
            raise RuntimeError(f"Missing {package}; run python -m pip install -r requirements.txt from the repository root.") from exc
        print(f"{package}: {actual}")
        if actual != expected:
            raise RuntimeError(f"{package} must be {expected}; install requirements.txt in the dedicated venv and restart the kernel.")
    # Import compiled libraries too: installed metadata alone does not prove ABI compatibility.
    for name in ("pandas", "numpy", "pyarrow", "pyspark", "psycopg2"):
        importlib.import_module(name)


def check_java():
    java_home = os.environ.get("JAVA_HOME")
    executable = "java.exe" if os.name == "nt" else "java"
    java = str(Path(java_home) / "bin" / executable) if java_home else shutil.which(executable)
    if not java or not Path(java).is_file():
        raise RuntimeError("Java not found. Select a JDK 17 installation using JAVA_HOME (the JDK directory, not bin), then reopen the terminal/kernel.")
    result = subprocess.run([java, "-version"], capture_output=True, text=True, timeout=20, check=True)
    output = result.stderr + result.stdout
    match = re.search(r'version\s+"(\d+)', output)
    if not match or int(match.group(1)) != 17:
        raise RuntimeError("This repository's supported Java baseline is JDK 17. Point JAVA_HOME to JDK 17 without replacing other Java installations.")
    print("Java:", output.splitlines()[0])


def worker_identity(_):
    import sys
    return sys.executable, tuple(sys.version_info[:2])


def check_spark():
    # Set these before creating any SparkContext; no local paths are hard-coded.
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    from pyspark.sql import SparkSession, functions as F

    spark = None
    try:
        spark = (SparkSession.builder.master("local[2]")
                 .appName("Interview environment preflight")
                 .config("spark.pyspark.python", sys.executable)
                 .config("spark.pyspark.driver.python", sys.executable)
                 .config("spark.sql.session.timeZone", "UTC")
                 .config("spark.sql.shuffle.partitions", "2")
                 .getOrCreate())
        spark.sparkContext.setLogLevel("ERROR")
        if spark.version != importlib.metadata.version("pyspark"):
            raise RuntimeError("Spark JVM and PySpark package versions differ; remove stale SPARK_HOME/PYTHONPATH overrides and restart.")
        workers = spark.sparkContext.parallelize([0, 1], 2).map(worker_identity).collect()
        for executable, version in workers:
            if version != tuple(sys.version_info[:2]) or Path(executable).resolve() != Path(sys.executable).resolve():
                raise RuntimeError(f"Worker Python differs from driver: {executable}, {version}. Restart the kernel after selecting the practice venv.")
        print(f"Spark {spark.version}: {spark.sparkContext.master}; both worker tasks match the active driver Python")

        @F.pandas_udf("long")
        def increment(values):
            return values + 1

        # Exercise the JVM, Python workers, Pandas and Arrow on two partitions.
        frame = spark.range(8, numPartitions=2).select(increment("id").alias("value"))
        result = frame.agg(F.count("value").alias("rows"), F.sum("value").alias("total")).first()
        if result.rows != 8 or result.total != 36:
            raise RuntimeError(f"Unexpected distributed smoke-test result: {result}")
        print("Distributed DataFrame / Pandas UDF / Arrow check: PASS (8 rows, sum 36)")
    except Exception as exc:
        raise RuntimeError(
            "Spark preflight failed. Verify JAVA_HOME, the selected venv, and local firewall/hostname settings. "
            "Remove stale SPARK_HOME/PYTHONPATH overrides when using pip-installed Spark; restart existing notebook kernels. "
            f"Underlying error: {type(exc).__name__}: {exc}"
        ) from exc
    finally:
        if spark is not None:
            spark.stop()


def main():
    try:
        check_packages()
        check_java()
        check_spark()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("Environment preflight: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
