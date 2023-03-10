"""empty message

Revision ID: 7648239125fc
Revises: 
Create Date: 2023-03-10 11:36:47.058675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7648239125fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Cats')
    # ### end Alembic commands ###
