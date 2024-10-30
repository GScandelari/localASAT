from datetime import datetime
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

def log_action(action):
    """Logs actions with date and time to logs/log.txt."""
    with open("logs/log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")
