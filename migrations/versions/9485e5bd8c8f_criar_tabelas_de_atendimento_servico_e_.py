"""criar tabelas de atendimento, servico e tabela associativa

Revision ID: 9485e5bd8c8f
Revises: 1f2bd7e0ac5d
Create Date: 2021-11-04 12:00:09.924635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9485e5bd8c8f'
down_revision = '1f2bd7e0ac5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=150), nullable=True),
    sa.Column('valor', sa.Float(precision=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atendimento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_atendimento_data'), 'atendimento', ['data'], unique=False)
    op.create_index(op.f('ix_atendimento_status'), 'atendimento', ['status'], unique=False)
    op.create_table('atendimento_servico',
    sa.Column('atendimento_id', sa.Integer(), nullable=True),
    sa.Column('servico_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atendimento_id'], ['atendimento.id'], ),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('atendimento_servico')
    op.drop_index(op.f('ix_atendimento_status'), table_name='atendimento')
    op.drop_index(op.f('ix_atendimento_data'), table_name='atendimento')
    op.drop_table('atendimento')
    op.drop_table('servico')
    # ### end Alembic commands ###
