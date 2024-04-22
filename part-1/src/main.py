from util.scheduler import Scheduler

def main():
    print("[INFO] Starting the scheduler")
    sc = Scheduler()
    sc.schedule_jobs()
if __name__ == '__main__':
    main()