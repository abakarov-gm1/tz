"""create products table

Revision ID: 9eb30ba1dfbc
Revises: 2f8d95d6c3d4
Create Date: 2025-01-01 15:51:36.882593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9eb30ba1dfbc'
down_revision: Union[str, None] = '2f8d95d6c3d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('products')