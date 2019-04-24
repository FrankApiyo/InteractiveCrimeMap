"""initial migration

Revision ID: 774efd73a0f1
Revises: 
Create Date: 2019-04-24 15:34:56.765062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '774efd73a0f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('crime', sa.Column('category', sa.Text(), nullable=False))
    op.alter_column('cartegory', sa.Column('category', sa.Text(), nullable=False))
    op.drop_column('crime', 'cartegory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crime', sa.Column('cartegory', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('crime', 'category')
    # ### end Alembic commands ###