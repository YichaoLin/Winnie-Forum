"""empty message

Revision ID: 072f7d40fe47
Revises: ca1335c7413a
Create Date: 2019-07-14 18:47:51.365866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '072f7d40fe47'
down_revision = 'ca1335c7413a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    # ### end Alembic commands ###