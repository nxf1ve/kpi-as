"""Создание пользователя и БД PostgreSQL для локальной разработки."""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def main() -> None:
    admin = dict(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432',
    )
    conn = psycopg2.connect(**admin)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_roles WHERE rolname = 'kpi'")
    if not cur.fetchone():
        cur.execute("CREATE USER kpi WITH PASSWORD 'kpi'")
        print('created user kpi')
    else:
        print('user kpi exists')

    cur.execute("SELECT 1 FROM pg_database WHERE datname = 'kpi_as'")
    if not cur.fetchone():
        cur.execute('CREATE DATABASE kpi_as OWNER kpi')
        print('created db kpi_as')
    else:
        print('db kpi_as exists')

    cur.execute('GRANT ALL PRIVILEGES ON DATABASE kpi_as TO kpi')
    cur.close()
    conn.close()

    conn = psycopg2.connect(
        dbname='kpi_as',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432',
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('GRANT ALL ON SCHEMA public TO kpi')
    cur.execute('ALTER SCHEMA public OWNER TO kpi')
    cur.close()
    conn.close()
    print('grants ok')

    conn = psycopg2.connect(
        dbname='kpi_as',
        user='kpi',
        password='kpi',
        host='localhost',
        port='5432',
    )
    conn.close()
    print('kpi login ok')


if __name__ == '__main__':
    main()
