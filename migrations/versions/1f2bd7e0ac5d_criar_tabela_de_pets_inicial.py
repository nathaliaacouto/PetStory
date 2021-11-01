"""criar tabela de pets inicial

Revision ID: 1f2bd7e0ac5d
Revises: 879bb8d5d260
Create Date: 2021-11-01 12:05:48.762271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f2bd7e0ac5d'
down_revision = '879bb8d5d260'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('raca', sa.String(length=50), nullable=True),
    sa.Column('pelagem', sa.String(length=50), nullable=True),
    sa.Column('obito', sa.Boolean(), nullable=True),
    sa.Column('dono_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dono_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pet_nome'), 'pet', ['nome'], unique=False)
    op.drop_index('ix_cliente_cep', table_name='cliente')
    op.drop_index('ix_cliente_cpf', table_name='cliente')
    op.drop_index('ix_cliente_endereco', table_name='cliente')
    op.drop_index('ix_cliente_telefone', table_name='cliente')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_cliente_telefone', 'cliente', ['telefone'], unique=False)
    op.create_index('ix_cliente_endereco', 'cliente', ['endereco'], unique=False)
    op.create_index('ix_cliente_cpf', 'cliente', ['cpf'], unique=False)
    op.create_index('ix_cliente_cep', 'cliente', ['cep'], unique=False)
    op.drop_index(op.f('ix_pet_nome'), table_name='pet')
    op.drop_table('pet')
    # ### end Alembic commands ###
