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
session_duration = 20            # Minutes
session_count = 1
scheduler = BackgroundScheduler()

# Constants
WORKTIME = int(0.8*session_duration)
RESTTIME = int(0.2*session_duration)

def Notify(msg):
    notification.notify(
        title="Welcome to FocusPal",
        message=msg,
        app_name="FocusPal",
        timeout=10,
        ticker="FP1.0"
    )

def StartDeepWork() -> int:
    global session_count, session_duration

    scheduler.add_job(Notify, 'interval', args=["Start Deep Work"], seconds=10, id='notify')

    print(f"Start deep work session #{session_count}? (Y/N)")
    response = input()


    if (response.lower() == 'y'):
        scheduler.remove_job('notify')

        session_duration = int(input("Duration (Minutes): "))
        WORKTIME = int(0.8*session_duration)
        RESTTIME = int(0.2*session_duration)

        # Deep Work Session
        start_time = datetime.now()
        print("Start time: ", start_time.strftime("%H:%M:%S"))
        with tqdm(total=WORKTIME) as pbar:
            # Cannot put the print statement between tqdm - update() else the progress bar will be splitted
            while True:
                elapsed = int((datetime.now() - start_time).total_seconds()/60)
                pbar.update(elapsed - pbar.n)
                # pbar.n = elapsed
                # pbar.refresh()

                if (elapsed >= WORKTIME):
                    break

                # time.sleep(60)

        # Rest Session
        start_time = datetime.now()
        print("Take a break!")
        scheduler.add_job(Notify, 'date', args=["Take a short break!"], run_date=datetime.now(), id='notify_rest')
        with tqdm(total=RESTTIME) as pbar:
            while True:
                elapsed = int((datetime.now() - start_time).total_seconds()/60)
                pbar.update(elapsed - pbar.n)

                if (elapsed >= RESTTIME):
                    scheduler.add_job(Notify, 'date', args=["Session Completed!"], run_date=datetime.now(), id='notify_end')
                    break

        stop_time = datetime.now()
        print("End time: ", stop_time.strftime("%H:%M:%S"))
        print("Session Completed!")
        session_count += 1
        return 0

    elif (response.lower() == 'n'):
        scheduler.remove_all_jobs()
        print("Session not started.")
    
    elif (response.lower() == 'exit'):
        return 1
    

def main():
    # scheduler.add_job(TimeBlocking, 'cron', hour=12, minute=0)
    # scheduler.add_job(StartDeepWork, 'interval', seconds=5)
    scheduler.start()
    while True:
        if (StartDeepWork() == 1):
            scheduler.remove_all_jobs()
            break
        
    # scheduler.start()



if __name__ == "__main__":
    main()