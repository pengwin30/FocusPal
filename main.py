# References:
# https://medium.com/@keshavmanglore/advanced-python-scheduler-scheduling-tasks-with-ap-scheduler-in-python-8c7998a4f116
# https://apscheduler.readthedocs.io/en/3.x/userguide.html
# https://www.geeksforgeeks.org/python/python-desktop-notifier-using-plyer-module/


# Features:
# NLP Chatbot - OpenAI API
# Time Blocking



from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta
from plyer import notification
from tqdm import tqdm

# Global variables
# Note: These are NOT constants! Since, we are changing their values in our process, these are just global variables.
start_time, stop_time = "", ""
session_duration = 20            # Seconds
session_count = 1
scheduler = BackgroundScheduler()

def Notify():
    notification.notify(
        title="Welcome to FocusPal",
        message="Start Deep Work",
        app_name="FocusPal",
        timeout=10,
        ticker="FP1.0"
    )

def StartDeepWork():
    global session_count

    scheduler.add_job(Notify, 'interval', seconds=5, id='notify')

    print(f"Start deep work session #{session_count}? (Y/N)")
    response = input()


    if (response.lower() == 'y'):
        start_time = datetime.now()
        print("Start time: ", start_time.strftime("%H:%M:%S"))

        scheduler.remove_job('notify')

        # while True:
        #     stop_time = datetime.now()
        #     elapsed_time = stop_time - start_time

        #     if (elapsed_time.total_seconds() >= 10):
        #         print("Session Completed!")
        #         break

        #     time.sleep(5)

        for i in tqdm(range(session_duration)):
            time.sleep(1)

        stop_time = datetime.now()
        print("End time: ", stop_time.strftime("%H:%M:%S"))
        print("Session Completed!")
        session_count += 1

    elif (response.lower() == 'n'):
        scheduler.remove_all_jobs()
        print("Session not started.")
    

def main():
    # scheduler.add_job(TimeBlocking, 'cron', hour=12, minute=0)
    # scheduler.add_job(StartDeepWork, 'interval', seconds=5)
    scheduler.start()
    while True:
        StartDeepWork()
    # scheduler.start()



if __name__ == "__main__":
    main()