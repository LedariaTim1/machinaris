#
# Performs an hourly insert of latest stats for the farm summary
#

import sqlite3
import traceback

from flask import g

from app import app, utils
from app.commands import global_config, chia_cli

DATABASE = '/root/.chia/machinaris/dbs/stats.db'


def get_db():
    db = getattr(g, '_stats_database', None)
    if db is None:
        db = g._stats_database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_stats_database', None)
    if db is not None:
        db.close()


def collect():
    if global_config.load()['plotting_only']:
        app.logger.info(
            "Skipping farm summary stats collection on plotting-only instance.")
        return
    with app.app_context():
        farm_summary = chia_cli.load_farm_summary()
        db = get_db()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO stat_plot_count (value) VALUES (?)",
                        (farm_summary.plot_count,))
        except:
            app.logger.info(traceback.format_exc())
        try:
            cur.execute("INSERT INTO stat_plots_size (value) VALUES (?)",
                        (utils.str_to_gibs(farm_summary.plot_size),))
        except:
            app.logger.info(traceback.format_exc())
        if farm_summary.status == "Farming":  # Only collect if fully synced
            try:
                cur.execute("INSERT INTO stat_total_chia (value) VALUES (?)",
                            (farm_summary.total_chia,))
            except:
                app.logger.info(traceback.format_exc())
            try:
                cur.execute("INSERT INTO stat_netspace_size (value) VALUES (?)",
                            (utils.str_to_gibs(farm_summary.network_size),))
            except:
                app.logger.info(traceback.format_exc())
            try:
                cur.execute("INSERT INTO stat_time_to_win (value) VALUES (?)",
                            (utils.etw_to_minutes(farm_summary.time_to_win),))
            except:
                app.logger.info(traceback.format_exc())
        db.commit()
