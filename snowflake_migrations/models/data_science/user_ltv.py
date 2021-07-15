from snowflake_migrations.models.base import AuditColumnMixin
from snowflake_migrations.models.data_science.base import Base

import sqlalchemy as sa

# test1
class UserLtv(AuditColumnMixin, Base):

    __tablename__ = "user_ltv"
    __table_args__ = {"schema": "data_science", "extend_existing": True}

    user_id = sa.Column(sa.types.BIGINT)
    consultation_completed_date = sa.Column(sa.types.DATE)
    consultation_completed_month = sa.Column(sa.types.DATE)
    channel = sa.Column(sa.types.TEXT)
    demo = sa.Column(sa.types.TEXT)
    signup_plan = sa.Column(sa.types.TEXT)
    formula_group = sa.Column(sa.types.TEXT)
    predicted_revenue = sa.Column(sa.types.FLOAT)
    predicted_gp = sa.Column(sa.types.FLOAT)
