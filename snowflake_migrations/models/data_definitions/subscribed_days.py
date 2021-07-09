import sqlalchemy as sa
from snowflake_migrations.models.base import Base, AuditColumnMixin


class SubscribedDays(AuditColumnMixin, Base):

    __tablename__ = "subscribed_days"
    __table_args__ = {"schema": "data_definitions", "extend_existing": True}

    user_id = sa.Column(sa.types.NUMERIC)
    date_pt = sa.Column(sa.types.DATE)
    was_paused = sa.Column(sa.types.BOOLEAN)
    consultaion_completed_at = sa.Column(sa.types.TIMESTAMP)
    first_shipment_delivered_at = sa.Column(sa.types.TIMESTAMP)
    first_full_payment_charged_at = sa.Column(sa.types.TIMESTAMP)
    referrer_type = sa.Column(sa.types.TEXT)
    trial_charged_at = sa.Column(sa.types.TIMESTAMP)
    is_vip = sa.Column(sa.types.BOOLEAN)
    large_superbottle = sa.Column(sa.types.NUMERIC)
    small_superbottle = sa.Column(sa.types.NUMERIC)
    large_rich_moisturizer = sa.Column(sa.types.NUMERIC)
    large_moisturizer = sa.Column(sa.types.NUMERIC)
    large_cleanser = sa.Column(sa.types.NUMERIC)
    large_acne_body_wash = sa.Column(sa.types.NUMERIC)
    large_hydrocolloid = sa.Column(sa.types.NUMERIC)
    large_dark_spot_formula	= sa.Column(sa.types.NUMERIC)
