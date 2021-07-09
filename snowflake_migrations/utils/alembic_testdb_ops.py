import os
import sqlalchemy as sa
import argparse
from distutils.util import strtobool


def testdb_create(create_test_db):
    snowflake_url = os.getenv("SNOWFLAKE_ADMIN_URL")
    target_db_name = os.getenv("SNOWFLAKE_CUROLOGY_DATABASE")
    alembic_test_db = os.getenv("ALEMBIC_TEST_DB")
    sf_engine = sa.create_engine(snowflake_url)
    sf_alembic_role = os.getenv("SNOWFLAKE_ALEMBIC_ROLE")
    with sf_engine.connect() as conn:
        if create_test_db:
            conn.execute(
                f"create or replace database {alembic_test_db} "
                f"clone {target_db_name};"
            )
            conn.execute(
                f"grant usage on database {alembic_test_db} "
                f"to role {sf_alembic_role};"
            )
        else:
            conn.execute(f"drop database if exists {alembic_test_db};")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("createdb", type=strtobool,
                        help="Create test db")
    args = parser.parse_args()
    if args.createdb:
        testdb_create(True)
    else:
        testdb_create(False)