"""empty message

Revision ID: da71a39b8e21
Revises: 
Create Date: 2021-12-12 19:03:26.248529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da71a39b8e21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_alerts():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alerts',
    sa.Column('unique_id', sa.String(length=128), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('priority', sa.String(length=64), nullable=False),
    sa.Column('service', sa.String(length=64), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('unique_id')
    )
    # ### end Alembic commands ###


def downgrade_alerts():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alerts')
    # ### end Alembic commands ###


def upgrade_blockchains():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockchains',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_blockchains():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blockchains')
    # ### end Alembic commands ###


def upgrade_challenges():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenges',
    sa.Column('unique_id', sa.String(length=64), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('challenge_id', sa.String(length=64), nullable=False),
    sa.Column('plots_past_filter', sa.String(length=32), nullable=False),
    sa.Column('proofs_found', sa.Integer(), nullable=False),
    sa.Column('time_taken', sa.String(length=32), nullable=False),
    sa.Column('created_at', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('unique_id')
    )
    # ### end Alembic commands ###


def downgrade_challenges():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('challenges')
    # ### end Alembic commands ###


def upgrade_connections():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connections',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_connections():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connections')
    # ### end Alembic commands ###


def upgrade_farms():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farms',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('mode', sa.String(length=32), nullable=False),
    sa.Column('status', sa.String(length=128), nullable=False),
    sa.Column('plot_count', sa.Integer(), nullable=False),
    sa.Column('plots_size', sa.REAL(), nullable=False),
    sa.Column('total_coins', sa.REAL(), nullable=False),
    sa.Column('netspace_size', sa.REAL(), nullable=False),
    sa.Column('expected_time_to_win', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_farms():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('farms')
    # ### end Alembic commands ###


def upgrade_keys():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keys',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_keys():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('keys')
    # ### end Alembic commands ###


def upgrade_partials():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partials',
    sa.Column('unique_id', sa.String(length=255), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('launcher_id', sa.String(length=255), nullable=False),
    sa.Column('pool_url', sa.String(length=255), nullable=False),
    sa.Column('pool_response', sa.String(), nullable=False),
    sa.Column('created_at', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('unique_id')
    )
    # ### end Alembic commands ###


def downgrade_partials():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('partials')
    # ### end Alembic commands ###


def upgrade_plotnfts():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plotnfts',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_plotnfts():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plotnfts')
    # ### end Alembic commands ###


def upgrade_plottings():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plottings',
    sa.Column('plot_id', sa.String(length=8), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('plotter', sa.String(length=64), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('k', sa.Integer(), nullable=False),
    sa.Column('tmp', sa.String(length=255), nullable=False),
    sa.Column('dst', sa.String(length=255), nullable=False),
    sa.Column('wall', sa.String(length=8), nullable=False),
    sa.Column('phase', sa.String(length=8), nullable=False),
    sa.Column('size', sa.String(length=8), nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('stat', sa.String(length=8), nullable=False),
    sa.Column('mem', sa.String(length=8), nullable=False),
    sa.Column('user', sa.String(length=8), nullable=False),
    sa.Column('sys', sa.String(length=8), nullable=False),
    sa.Column('io', sa.String(length=8), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('plot_id')
    )
    # ### end Alembic commands ###


def downgrade_plottings():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plottings')
    # ### end Alembic commands ###


def upgrade_plots():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plots',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('displayname', sa.String(length=255), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('plot_id', sa.String(length=16), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=False),
    sa.Column('dir', sa.String(length=255), nullable=False),
    sa.Column('file', sa.String(length=255), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('plot_check', sa.String(length=255), nullable=True),
    sa.Column('plot_analyze', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.String(length=64), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'plot_id')
    )
    # ### end Alembic commands ###


def downgrade_plots():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plots')
    # ### end Alembic commands ###


def upgrade_pools():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pools',
    sa.Column('unique_id', sa.String(length=255), nullable=False),
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('launcher_id', sa.String(length=255), nullable=False),
    sa.Column('login_link', sa.String(), nullable=True),
    sa.Column('pool_state', sa.String(), nullable=False),
    sa.Column('updated_at', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('unique_id')
    )
    # ### end Alembic commands ###


def downgrade_pools():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pools')
    # ### end Alembic commands ###


def upgrade_wallets():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallets',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('cold_balance', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'blockchain')
    )
    # ### end Alembic commands ###


def downgrade_wallets():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    # ### end Alembic commands ###


def upgrade_workers():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workers',
    sa.Column('hostname', sa.String(length=255), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('displayname', sa.String(length=255), nullable=True),
    sa.Column('mode', sa.String(length=64), nullable=False),
    sa.Column('services', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('config', sa.String(), nullable=False),
    sa.Column('latest_ping_result', sa.String(), nullable=True),
    sa.Column('ping_success_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('hostname', 'port')
    )
    # ### end Alembic commands ###


def downgrade_workers():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workers')
    # ### end Alembic commands ###


def upgrade_stat_plot_count():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plot_count',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plot_count():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plot_count')
    # ### end Alembic commands ###


def upgrade_stat_plots_size():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plots_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plots_size():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plots_size')
    # ### end Alembic commands ###


def upgrade_stat_total_coins():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_total_coins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_total_coins():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_total_coins')
    # ### end Alembic commands ###


def upgrade_stat_netspace_size():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_netspace_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_netspace_size():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_netspace_size')
    # ### end Alembic commands ###


def upgrade_stat_time_to_win():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_time_to_win',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_time_to_win():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_time_to_win')
    # ### end Alembic commands ###


def upgrade_stat_plots_total_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plots_total_used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plots_total_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plots_total_used')
    # ### end Alembic commands ###


def upgrade_stat_plots_disk_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plots_disk_used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plots_disk_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plots_disk_used')
    # ### end Alembic commands ###


def upgrade_stat_plots_disk_free():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plots_disk_free',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plots_disk_free():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plots_disk_free')
    # ### end Alembic commands ###


def upgrade_stat_plotting_total_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plotting_total_used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('blockchain', sa.String(length=64), nullable=False),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plotting_total_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plotting_total_used')
    # ### end Alembic commands ###


def upgrade_stat_plotting_disk_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plotting_disk_used',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plotting_disk_used():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plotting_disk_used')
    # ### end Alembic commands ###


def upgrade_stat_plotting_disk_free():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_plotting_disk_free',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('value', sa.REAL(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_stat_plotting_disk_free():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_plotting_disk_free')
    # ### end Alembic commands ###

