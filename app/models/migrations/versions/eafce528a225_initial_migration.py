"""initial migration

Revision ID: eafce528a225
Revises: 108541aeec62
Create Date: 2024-08-29 12:09:40.539267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eafce528a225'
down_revision: Union[str, None] = '108541aeec62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
