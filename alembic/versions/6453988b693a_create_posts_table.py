"""create posts table

Revision ID: 6453988b693a
Revises: 
Create Date: 2022-10-25 13:45:59.602560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '645398b8693a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
