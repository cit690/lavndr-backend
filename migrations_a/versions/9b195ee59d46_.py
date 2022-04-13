"""empty message

Revision ID: 9b195ee59d46
Revises: 450d7e1b301c
Create Date: 2022-04-11 16:10:59.922466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b195ee59d46'
down_revision = '450d7e1b301c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('dob', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('vibe_check', sa.String(length=200), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('sun_sign', sa.String(), nullable=True),
    sa.Column('moon_sign', sa.String(), nullable=True),
    sa.Column('rising_sign', sa.String(), nullable=True),
    sa.Column('profile_picture', sa.String(), nullable=True),
    sa.Column('gender_identity', sa.String(), nullable=True),
    sa.Column('orientation', sa.String(), nullable=True),
    sa.Column('smoke', sa.Boolean(), nullable=True),
    sa.Column('drink', sa.Boolean(), nullable=True),
    sa.Column('four_twenty', sa.Boolean(), nullable=True),
    sa.Column('is_sober', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###