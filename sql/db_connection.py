"""Shared PostgreSQL connection settings for all SQL practice notebooks.

Edit db_config.ini once; do not commit it to a public repository.
"""
from configparser import ConfigParser
from pathlib import Path
import psycopg2

_CONFIG_PATH = Path(__file__).resolve().with_name("db_config.ini")


def connection_settings():
    if not _CONFIG_PATH.is_file():
        raise FileNotFoundError(
            f"Missing {_CONFIG_PATH}. Copy db_config.example.ini to "
            "db_config.ini, then set your PostgreSQL credentials there. "
            "Keep db_config.ini out of Git."
        )
    parser = ConfigParser(interpolation=None)
    parser.read(_CONFIG_PATH, encoding="utf-8")
    if "postgresql" not in parser:
        raise ValueError(f"Missing [postgresql] section in {_CONFIG_PATH}")
    section = parser["postgresql"]
    required = ("host", "port", "dbname", "user")
    missing = [key for key in required if not section.get(key, "").strip()]
    if missing:
        raise ValueError(f"Missing PostgreSQL setting(s) in {_CONFIG_PATH}: {', '.join(missing)}")
    options = {"host": section["host"], "port": section.getint("port"),
               "dbname": section["dbname"], "user": section["user"]}
    # Empty password lets libpq use peer/trust/.pgpass/PGPASSWORD where configured.
    if section.get("password", ""):
        options["password"] = section["password"]
    return options


def connect(*, autocommit=True):
    conn = psycopg2.connect(**connection_settings())
    conn.autocommit = autocommit
    return conn
