import os

import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)
db = client.logsdb
logs_collection = db.logs

def read_logs_warnings(n=100):
    filter = {"hardware_stats.ram_usage_percent": {"$gte": 80}}
    logs_warning = logs_collection.find(filter).sort("timestamp", -1).limit(n)

    found = 0

    resultado_texto = ""
    resultado_texto += "-" * 30 + "\n"

    for log in logs_warning:
        found += 1
        resultado_texto += f"Warning! High RAM usage: {log['hardware_stats']['ram_usage_percent']}%\n"
        resultado_texto += f"Date/Hour: {log.get('timestamp')}\n"
        resultado_texto += "-" * 30 + "\n"
        if found == n:
            break
    if found == 0:
        return "Nenhum warning encontrado"
    return resultado_texto

def read_logs_ok(n=100):
    filter = {"hardware_stats.ram_usage_percent": {"$lt": 80}}
    logs_ok = logs_collection.find(filter).sort("timestamp", -1).limit(n)

    found = 0

    resultado_texto = ""
    resultado_texto += "-" * 30 + "\n"

    for log in logs_ok:
        found += 1
        resultado_texto += f"All right! Low RAM usage: {log['hardware_stats']['ram_usage_percent']}%\n"
        resultado_texto += f"Date/Hour: {log.get('timestamp')}\n"
        resultado_texto += "-" * 30 + "\n"
        if found == n:
            break
    if found == 0:
        return "Nenhum log encontrado"
    return resultado_texto

if __name__ == "__main__":

    client.close()