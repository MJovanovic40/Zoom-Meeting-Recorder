import schedule
import time
from meeting_handler import record_meeting


def initialize_shedule(subjects):
    print("Making a Schedule...")
    for i in subjects:
        if i.day == "Ponedeljak":
            schedule.every().monday.at(i.start_time).do(record_meeting, i)
        elif i.day == "Utorak":
            schedule.every().tuesday.at(i.start_time).do(record_meeting, i)
        elif i.day == "Sreda":
            schedule.every().wednesday.at(i.start_time).do(record_meeting, i)
        elif i.day == "Cetvrtak":
            schedule.every().thursday.at(i.start_time).do(record_meeting, i)
        elif i.day == "Petak":
            schedule.every().friday.at(i.start_time).do(record_meeting, i)

    if len(subjects) > 0:
        print("Running Schedule...")
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("No subjects to monitor.")