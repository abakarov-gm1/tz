"""Create Users

Revision ID: 2f8d95d6c3d4
Revises: 
Create Date: 2025-01-01 15:19:44.663610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2f8d95d6c3d4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('name', sa.String, nullable=False),
                    sa.Column('email', sa.String, nullable=True),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('role', sa.String, nullable=False),
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###