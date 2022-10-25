"""add a new column to posts table

Revision ID: 8658dc7a8fe4
Revises: 645398b8693a
Create Date: 2022-10-25 16:01:28.863361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8658dc7a8fe4'
down_revision = '645398b8693a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts",'content')
