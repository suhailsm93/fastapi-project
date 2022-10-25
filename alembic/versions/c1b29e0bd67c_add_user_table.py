"""add user table

Revision ID: c1b29e0bd67c
Revises: 8658dc7a8fe4
Create Date: 2022-10-25 17:25:16.937249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1b29e0bd67c'
down_revision = '8658dc7a8fe4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table("users")
