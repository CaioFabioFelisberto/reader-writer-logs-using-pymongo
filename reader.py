import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
db = client.logsdb
logs_collection = db.logs

def read_logs_warnings(n=100):
    filter = {"hardware_stats.ram_usage_percent": {"$gte": 80}}
    logs_warning = logs_collection.find(filter)

    found = 0
    print("-" * 30)
    for log in logs_warning:
        found += 1
        print(F"Warning! High RAM usage: {log['hardware_stats']['ram_usage_percent']}%")
        print(f"Date/Hour: {log.get('timestamp')}")
        print("-" * 30)
        if found == n:
            return

def read_logs_ok(n=100):
    filter = {"hardware_stats.ram_usage_percent": {"$lt": 80}}
    logs_ok = logs_collection.find(filter)

    found = 0
    print("-" * 30)
    for log in logs_ok:
        found += 1
        print(F"All right! Low RAM usage: {log['hardware_stats']['ram_usage_percent']}%")
        print(f"Date/Hour: {log.get('timestamp')}")
        print("-" * 30)
        if found == n:
            return

read_logs_warnings()
read_logs_ok()

client.close()