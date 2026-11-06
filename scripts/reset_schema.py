"""
Пересоздание schema public в PostgreSQL.
Нужно при смене AUTH_USER_MODEL после уже применённых миграций auth.
"""

import os
import sys
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / '.env')


def main() -> None:
    if os.getenv('USE_SQLITE', '0') == '1':
        db_path = ROOT / 'db.sqlite3'
        if db_path.exists():
            db_path.unlink()
            print(f'removed {db_path}')
        else:
            print('sqlite db not found (ok)')
        return

    dbname = os.getenv('POSTGRES_DB', 'kpi_as')
    user = os.getenv('POSTGRES_USER', 'kpi')
    password = os.getenv('POSTGRES_PASSWORD', 'kpi')
    host = os.getenv('POSTGRES_HOST', 'localhost')
    port = os.getenv('POSTGRES_PORT', '5432')

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('DROP SCHEMA public CASCADE')
    cur.execute('CREATE SCHEMA public')
    cur.execute('GRANT ALL ON SCHEMA public TO CURRENT_USER')
    cur.execute('GRANT ALL ON SCHEMA public TO public')
    cur.close()
    conn.close()
    print(f'schema public reset in {dbname}')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f'error: {exc}', file=sys.stderr)
        sys.exit(1)
