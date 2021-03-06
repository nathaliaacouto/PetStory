"""adicionar campo de idade para pets e obs

Revision ID: 5bccdb86a511
Revises: 9485e5bd8c8f
Create Date: 2021-11-10 15:53:16.187956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bccdb86a511'
down_revision = '9485e5bd8c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('atendimento', schema=None) as batch_op:
        batch_op.add_column(sa.Column('obs', sa.String(length=200), nullable=True))

    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('idade', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet', schema=None) as batch_op:
        batch_op.drop_column('idade')

    with op.batch_alter_table('atendimento', schema=None) as batch_op:
        batch_op.drop_column('obs')

    # ### end Alembic commands ###
