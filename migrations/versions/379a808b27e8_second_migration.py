"""second migration

Revision ID: 379a808b27e8
Revises: 167e1bdb6c49
Create Date: 2017-12-05 19:52:59.202768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '379a808b27e8'
down_revision = '167e1bdb6c49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('content_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topics', 'content_html')
    # ### end Alembic commands ###
