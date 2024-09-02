"""initial migration

Revision ID: cc509dba3d81
Revises: b8508df01a15
Create Date: 2024-08-29 12:37:23.796968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc509dba3d81'
down_revision: Union[str, None] = 'b8508df01a15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
