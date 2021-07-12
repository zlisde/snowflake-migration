import sqlalchemy as sa
from snowflake_migrations.models.base import AuditColumnMixin
from snowflake_migrations.models.dm_datascience.base import Base


class UserLtv(AuditColumnMixin, Base):

    __tablename__ = "user_ltv"
    __table_args__ = {"schema": "dm_datascience", "extend_existing": True}
#test11111

    user_id = sa.Column(sa.types.BIGINT)
    consultation_completed_date = sa.Column(sa.types.DATE)
    consultation_completed_month = sa.Column(sa.types.DATE)
    channel = sa.Column(sa.types.TEXT)
    demo = sa.Column(sa.types.TEXT)
    signup_plan = sa.Column(sa.types.TEXT)
    formula_group = sa.Column(sa.types.TEXT)
    predicted_revenue = sa.Column(sa.types.FLOAT)
    predicted_gp = sa.Column(sa.types.FLOAT)
