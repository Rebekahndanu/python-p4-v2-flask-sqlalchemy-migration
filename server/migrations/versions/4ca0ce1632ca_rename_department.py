"""rename department

Revision ID: 4ca0ce1632ca
Revises: 3ab4ac37ed47
Create Date: 2024-04-04 04:58:18.648342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ca0ce1632ca'
down_revision = '3ab4ac37ed47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
