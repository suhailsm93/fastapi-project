"""add foregin-key to posts table

Revision ID: ad0758a75bac
Revises: c1b29e0bd67c
Create Date: 2022-10-25 17:38:57.884747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad0758a75bac'
down_revision = 'c1b29e0bd67c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
     local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column("posts", 'owner_id')
