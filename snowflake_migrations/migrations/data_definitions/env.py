import json
import os
import pathlib
from logging.config import fileConfig

from alembic import context
from alembic.ddl.impl import DefaultImpl

from snowflake.sqlalchemy import URL

from sqlalchemy import create_engine


class SnowflakeImpl(DefaultImpl):
    __dialect__ = "snowflake"


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from snowflake_migrations.models.data_definitions.base import Base  # noqa E402
from snowflake_migrations.models import data_definitions  # noqa E402

target_metadata = Base.metadata
# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    sf_url_dict = json.loads(os.getenv("SNOWFLAKE_URL"))
    sf_env = os.getenv("SNOWFLAKE_ENV")
    if sf_env == "prod":
        sf_database = os.getenv("SNOWFLAKE_CUROLOGY_DATABASE")
    else:
        sf_database = os.getenv("ALEMBIC_TEST_DB")
    sf_schema = os.path.basename(pathlib.Path(__file__).parent.resolve())
    sf_url_dict["database"] = sf_database
    sf_url_dict["schema"] = sf_schema
    return sf_url_dict


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    connectable = create_engine(URL(**get_url()))
    context.configure(
        connection=connectable.connect(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    sf_schema = os.path.basename(pathlib.Path(__file__).parent.resolve())

    def process_revision_directives(context, revision, directives):
        if config.cmd_opts.autogenerate:
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []

    connectable = create_engine(URL(**get_url()))
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema="utility",
            version_table=f"{sf_schema}_alembic_version",
            process_revision_directives=process_revision_directives,
            compare_types=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()