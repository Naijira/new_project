"""Add roles and users tables

Revision ID: fc78328a4756
Revises: 8e381ecbe3ea
Create Date: 2024-05-30 13:03:00.881259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc78328a4756'
down_revision: Union[str, None] = '8e381ecbe3ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
