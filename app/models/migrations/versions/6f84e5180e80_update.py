"""update

Revision ID: 6f84e5180e80
Revises: 4b30a55c2451
Create Date: 2024-08-28 11:46:19.328402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f84e5180e80'
down_revision: Union[str, None] = '4b30a55c2451'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
