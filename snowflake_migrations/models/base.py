import sqlalchemy as sa


from sqlalchemy.orm import declarative_mixin
from sqlalchemy.orm import declared_attr

#


@declarative_mixin
class AuditColumnMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    row_id = sa.Column(sa.types.BIGINT, autoincrement=True, primary_key=True)
    _lattice_exec_date_utc = sa.Column(sa.types.TIMESTAMP)
    _snowflake_synced_utc = sa.Column(sa.types.TIMESTAMP)
