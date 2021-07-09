import sqlalchemy as sa
from snowflake_migrations.models.base import Base, AuditColumnMixin


class Retention(AuditColumnMixin, Base):

    __tablename__ = "retention"
    __table_args__ = {"schema": "data_definitions", "extend_existing": True}
# test112
    date = sa.Column(sa.types.Date)
    retention_days = sa.Column(sa.types.NUMERIC)
    date_param = sa.Column(sa.types.TEXT)
    brand_id = sa.Column(sa.NUMERIC)
    retention_rate = sa.Column(sa.FLOAT)
