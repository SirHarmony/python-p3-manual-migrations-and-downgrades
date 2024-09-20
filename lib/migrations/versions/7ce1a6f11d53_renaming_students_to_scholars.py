"""Renaming students to scholars

Revision ID: 7ce1a6f11d53
Revises: 791279dd0760
Create Date: 2024-09-20 15:55:36.857693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ce1a6f11d53'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
