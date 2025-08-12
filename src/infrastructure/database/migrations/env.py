import os
import sys
from logging.config import fileConfig

from alembic import context


# Add src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from infrastructure.database.session import sync_postgresql_engine

# import SQLAlchemy models
import infrastructure.database.models.base as base  # noqa: F401

import domains.casting_patterns.models  # noqa: F401
import domains.casting_products.models  # noqa: F401
import domains.casting_technologies.models  # noqa: F401
import domains.iron_oxides.models  # noqa: F401
import domains.mold_core_batches.models  # noqa: F401
import domains.mold_core_making_machines.models  # noqa: F401
import domains.mold_core_types.models  # noqa: F401
import domains.mold_passports.models  # noqa: F401
import domains.molding_areas.models  # noqa: F401
import domains.molding_flasks.models  # noqa: F401
import domains.molding_sand_types.models  # noqa: F401
import domains.pattern_plate_frames.models  # noqa: F401
import domains.resins.models  # noqa: F401
import domains.triethylamines.models  # noqa: F401


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here for 'autogenerate' support
# from infrastructure.database.models.base import BaseORM
target_metadata = base.BaseORM.metadata


# other values from the config, defined by the needs of env.py, can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the script output.
    """
    connectable = sync_postgresql_engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a connection with the context.
    """
    connectable = sync_postgresql_engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
