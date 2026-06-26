"""add is_active

Revision ID: 5e0337b23ab3
Revises: d3c6bdae41e6
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision = '5e0337b23ab3'
down_revision = 'd3c6bdae41e6'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column(
        'students',
        sa.Column(
            'is_active',
            sa.Boolean(),
            server_default='1',
            nullable=True
        )
    )


def downgrade():

    op.drop_column(
        'students',
        'is_active'
    )