from snowflake_migrations.models.data_definitions.base import Base

import sqlalchemy as sa

# test11
class SubscribedDays(Base):

    __tablename__ = "subscribed_days"
    __table_args__ = {"schema": "data_definitions", "extend_existing": True}

    _lattice_exec_date_utc = sa.Column(sa.types.TIMESTAMP)
    _snowflake_synced_utc = sa.Column(sa.types.TIMESTAMP)
    user_id = sa.Column(sa.types.NUMERIC, primary_key=True)
    date_pt = sa.Column(sa.types.DATE)
    was_paused = sa.Column(sa.types.BOOLEAN)
    consultation_completed_at = sa.Column(sa.types.TIMESTAMP)
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
    large_dark_spot_formula = sa.Column(sa.types.NUMERIC)
    large_future_formula = sa.Column(sa.types.NUMERIC)
