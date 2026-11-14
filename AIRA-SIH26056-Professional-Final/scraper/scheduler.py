from apscheduler.schedulers.blocking import BlockingScheduler
from scraper.playwright_adapter import PermittedSourceAdapter
def run(): print(PermittedSourceAdapter().collect("DEL-BOM","YYYY-MM-DD"))
if __name__=="__main__":
 s=BlockingScheduler();s.add_job(run,"cron",hour=6,minute=0);print("AIRA daily scheduler started");s.start()
