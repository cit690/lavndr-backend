"""empty message

Revision ID: 450d7e1b301c
Revises: a3d4a2b9ab51
Create Date: 2022-04-11 16:05:26.321327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450d7e1b301c'
down_revision = 'a3d4a2b9ab51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'dob')
    op.drop_column('profiles', 'smoke')
    op.drop_column('profiles', 'bio')
    op.drop_column('profiles', 'four_twenty')
    op.drop_column('profiles', 'vibe_check')
    op.drop_column('profiles', 'orientation')
    op.drop_column('profiles', 'sun_sign')
    op.drop_column('profiles', 'is_sober')
    op.drop_column('profiles', 'profile_picture')
    op.drop_column('profiles', 'location')
    op.drop_column('profiles', 'drink')
    op.drop_column('profiles', 'moon_sign')
    op.drop_column('profiles', 'gender_identity')
    op.drop_column('profiles', 'rising_sign')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('rising_sign', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('gender_identity', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('moon_sign', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('drink', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('profile_picture', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('is_sober', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('sun_sign', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('orientation', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('vibe_check', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('four_twenty', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('bio', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('smoke', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('dob', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
