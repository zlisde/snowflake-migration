# flake8: noqa
"""empty message

Revision ID: 0e6514ed57de
Revises: 
Create Date: 2021-07-15 05:01:16.864337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0e6514ed57de"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "retention",
        sa.Column("row_id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("_lattice_exec_date_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column("_snowflake_synced_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "_lattice_s3_partition_date_utc", sa.TIMESTAMP(), nullable=True
        ),
        sa.Column("date", sa.Date(), nullable=True),
        sa.Column("retention_days", sa.NUMERIC(), nullable=True),
        sa.Column("date_param", sa.TEXT(), nullable=True),
        sa.Column("brand_id", sa.NUMERIC(), nullable=True),
        sa.Column("retention_rate", sa.FLOAT(), nullable=True),
        sa.PrimaryKeyConstraint("row_id"),
        schema="data_definitions",
    )
    op.create_table(
        "subscribed_days",
        sa.Column("_lattice_exec_date_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column("_snowflake_synced_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column("user_id", sa.NUMERIC(), nullable=False),
        sa.Column("date_pt", sa.DATE(), nullable=True),
        sa.Column("was_paused", sa.BOOLEAN(), nullable=True),
        sa.Column("consultation_completed_at", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "first_shipment_delivered_at", sa.TIMESTAMP(), nullable=True
        ),
        sa.Column(
            "first_full_payment_charged_at", sa.TIMESTAMP(), nullable=True
        ),
        sa.Column("referrer_type", sa.TEXT(), nullable=True),
        sa.Column("trial_charged_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("is_vip", sa.BOOLEAN(), nullable=True),
        sa.Column("large_superbottle", sa.NUMERIC(), nullable=True),
        sa.Column("small_superbottle", sa.NUMERIC(), nullable=True),
        sa.Column("large_rich_moisturizer", sa.NUMERIC(), nullable=True),
        sa.Column("large_moisturizer", sa.NUMERIC(), nullable=True),
        sa.Column("large_cleanser", sa.NUMERIC(), nullable=True),
        sa.Column("large_acne_body_wash", sa.NUMERIC(), nullable=True),
        sa.Column("large_hydrocolloid", sa.NUMERIC(), nullable=True),
        sa.Column("large_dark_spot_formula", sa.NUMERIC(), nullable=True),
        sa.Column("large_future_formula", sa.NUMERIC(), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
        schema="data_definitions",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscribed_days", schema="data_definitions")
    op.drop_table("retention", schema="data_definitions")
    # ### end Alembic commands ###
