from time import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job1():
    print("Job 1: %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def job2():
    print("Job 2: %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def job3():
    print("Job 3")

def job4():
    print("Job 4")

scheduler = BlockingScheduler(timezone="Asia/Shanghai")

# 使用add_job方法設定不同的定期任務
scheduler.add_job(job1, 'interval', minutes=1)
scheduler.add_job(job2, 'interval', seconds=5)
scheduler.add_job(job3, 'interval', seconds=3)

# 使用cron表達式，設定在星期一至星期六的每週15:16執行job4函數
scheduler.add_job(job4, 'cron', day_of_week='1-6', hour=15, minute=16)

# 啟動定時任務
scheduler.start()
