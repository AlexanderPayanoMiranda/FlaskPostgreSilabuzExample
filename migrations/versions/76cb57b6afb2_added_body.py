"""Added body

Revision ID: 76cb57b6afb2
Revises: 59e90fd5a012
Create Date: 2023-01-25 11:47:00.521380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76cb57b6afb2'
down_revision = '59e90fd5a012'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('body')

    # ### end Alembic commands ###
