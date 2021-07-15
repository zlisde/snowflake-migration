import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr


class AuditColumnMixin:
    @declared_attr
    def __tablename__(cls):  # noqa N805
        return cls.__name__.lower()

    row_id = sa.Column(sa.types.BIGINT, autoincrement=True, primary_key=True)
    _lattice_exec_date_utc = sa.Column(sa.types.TIMESTAMP)
    _snowflake_synced_utc = sa.Column(sa.types.TIMESTAMP)
    _lattice_s3_partition_date_utc = sa.Column(sa.types.TIMESTAMP)
