"""add reservation

Revision ID: aa3223662f88
Revises: a99a82611464
Create Date: 2024-08-07 22:09:18.589966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa3223662f88'
down_revision = 'a99a82611464'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation', sa.Column('to_reserve', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'to_reserve')
    # ### end Alembic commands ###
