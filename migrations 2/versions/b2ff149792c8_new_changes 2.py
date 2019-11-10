"""new_changes

Revision ID: b2ff149792c8
Revises: 8c11049a3130
Create Date: 2019-10-31 09:04:59.354021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ff149792c8'
down_revision = '8c11049a3130'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prescription', sa.Column('prescription_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prescription', 'prescription_id')
    # ### end Alembic commands ###
