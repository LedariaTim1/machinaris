import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from api import app
from api.schedules import status_worker, status_farm, status_plotting, \
    status_plots, status_challenges, status_wallets, status_blockchains, \
    status_connections, status_keys
from api.schedules import stats_disk, stats_farm

scheduler = BackgroundScheduler()

# Statistics gathering locally
#scheduler.add_job(func=stats_farm.collect, trigger='cron', minute=0)  # Hourly
#scheduler.add_job(func=stats_disk.collect, trigger='cron', minute="*/5") # Every 5 minutes

# Testing only
#scheduler.add_job(func=stats_farm.collect, trigger='interval', seconds=20) # Test immediately
#scheduler.add_job(func=stats_disk.collect, trigger='interval', seconds=20) # Test immediately

# Status gathering - reported via API
scheduler.add_job(func=status_worker.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_farm.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_plotting.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_plots.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_challenges.update, trigger='interval', seconds=5) 
scheduler.add_job(func=status_wallets.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_blockchains.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_connections.update, trigger='interval', seconds=30) 
scheduler.add_job(func=status_keys.update, trigger='interval', seconds=30) 

scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())