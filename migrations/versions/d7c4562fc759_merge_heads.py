"""Merge heads

Revision ID: d7c4562fc759
Revises: cc6753406f7a, 885f57519cdf
Create Date: 2024-06-01 17:07:28.803815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7c4562fc759'
down_revision = ('cc6753406f7a', '885f57519cdf')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
