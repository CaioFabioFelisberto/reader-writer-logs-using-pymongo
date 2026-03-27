import os
import datetime
import time
import psutil
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
db = client.logsdb
logs_collection = db.logs

def write_logs(n=2, interval=5):
    for i in range(n):

        mem = psutil.virtual_memory()

        mem_total = round(mem.total / (1024 ** 3), 2)
        mem_used = round(mem.used / (1024 ** 3), 2)

        logs_collection.insert_one({
        "timestamp": datetime.datetime.now(),
        "origem": "Monitor_Sistema",
        "status": "OK",
        "hardware_stats": {
            "total_ram_gb": mem_total,
            "total_ram_usage_gb": mem_used,
            "ram_usage_percent": mem.percent
        },
        "tags": ["estudo", "python", "dev"]
    })

        print(f"Log {i+1} adicionado.")

        time.sleep(interval)

if __name__ == "__main__":

    client.close()
