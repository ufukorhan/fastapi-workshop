"""add user table

Revision ID: 79574871d3bd
Revises: 132f7ba26d1b
Create Date: 2022-08-01 19:00:58.072150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79574871d3bd'
down_revision = '132f7ba26d1b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
