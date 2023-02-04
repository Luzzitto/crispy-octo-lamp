from db import DB
from datetime import datetime

def log_message(program: str, message: str, level: str, timestamp: datetime=datetime.now()):
    db = DB()
    db.query(f"INSERT INTO logs (`program`, `message`, `level`, `timestamp`) VALUES (%s, %s, %s, %s)", (program, message, level, timestamp.strftime('%Y-%m-%d %H:%M:%S')))