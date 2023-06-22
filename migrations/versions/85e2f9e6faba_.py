"""empty message

Revision ID: 85e2f9e6faba
Revises: 7fecb5054257
Create Date: 2023-06-22 19:20:41.104571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85e2f9e6faba'
down_revision = '7fecb5054257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('opinion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('source', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('added_by', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('text')
    )
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_opinion_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_opinion_timestamp'))

    op.drop_table('opinion')
    # ### end Alembic commands ###
