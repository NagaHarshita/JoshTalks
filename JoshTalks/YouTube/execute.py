from apscheduler.schedulers.background import BackgroundScheduler
from . import views
scheduler = BackgroundScheduler()
scheduler.add_job(views.GetVideos, 'interval', seconds=10)
scheduler.start()
