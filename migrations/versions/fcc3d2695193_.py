"""empty message

Revision ID: fcc3d2695193
Revises: 31c34bde627b
Create Date: 2023-08-11 16:17:27.241885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcc3d2695193'
down_revision = '31c34bde627b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('abled', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('ban', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('activity', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('member', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('level', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('level')
        batch_op.drop_column('member')
        batch_op.drop_column('activity')
        batch_op.drop_column('ban')
        batch_op.drop_column('abled')

    # ### end Alembic commands ###