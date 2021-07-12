"""empty message

Revision ID: 3de0f052817a
Revises: 
Create Date: 2021-07-12 13:55:55.002470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3de0f052817a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_ltv",
        sa.Column("row_id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("_lattice_exec_date_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column("_snowflake_synced_utc", sa.TIMESTAMP(), nullable=True),
        sa.Column("user_id", sa.BIGINT(), nullable=True),
        sa.Column("consultation_completed_date", sa.DATE(), nullable=True),
        sa.Column("consultation_completed_month", sa.DATE(), nullable=True),
        sa.Column("channel", sa.TEXT(), nullable=True),
        sa.Column("demo", sa.TEXT(), nullable=True),
        sa.Column("signup_plan", sa.TEXT(), nullable=True),
        sa.Column("formula_group", sa.TEXT(), nullable=True),
        sa.Column("predicted_revenue", sa.FLOAT(), nullable=True),
        sa.Column("predicted_gp", sa.FLOAT(), nullable=True),
        sa.PrimaryKeyConstraint("row_id"),
        schema="dm_datascience",
    )
    op.drop_table("alembic_version")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "alembic_version",
        sa.Column(
            "version_num",
            sa.VARCHAR(length=32),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("version_num"),
    )
    op.drop_table("user_ltv", schema="dm_datascience")
    # ### end Alembic commands ###
