# References:
# https://medium.com/@keshavmanglore/advanced-python-scheduler-scheduling-tasks-with-ap-scheduler-in-python-8c7998a4f116
# https://apscheduler.readthedocs.io/en/3.x/userguide.html
# https://www.geeksforgeeks.org/python/python-desktop-notifier-using-plyer-module/


# Features:
# NLP Chatbot - OpenAI API
# Time Blocking



from apscheduler.schedulers.background import BackgroundScheduler
import time
from plyer import notification


def TimeBlocking():
    notification.notify(
        title="Welcome to FocusPal",
        message="Begin Deep Work",
        app_name="FocusPal",
        timeout=10,
        ticker="FP1.0"
    )


scheduler = BackgroundScheduler()
# scheduler.add_job(TimeBlocking, 'cron', hour=12, minute=0)
scheduler.add_job(TimeBlocking, 'interval', seconds=5)
scheduler.start()

while True:
    time.sleep(1)