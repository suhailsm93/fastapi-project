"""add remaining columns to posts table

Revision ID: 609c906a0175
Revises: ad0758a75bac
Create Date: 2022-10-25 17:52:44.925821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '609c906a0175'
down_revision = 'ad0758a75bac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column("posts", sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, 
    server_default=sa.text('now()')))


def downgrade():
    op.drop_column("posts", 'published')
    op.drop_column("posts", 'created_at')
