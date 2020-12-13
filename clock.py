from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from Twilio_Whatsapp import spam

# def job_function():
#     print("Hello World")

sched = BlockingScheduler()

# Schedule spam to be called every two hours
sched.add_job(spam, 'interval', seconds=2)

sched.start()