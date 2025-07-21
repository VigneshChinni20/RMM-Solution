def restart_service():
    print("Restarting system service...")

def log_event(message):
    with open("rmm_log.txt", "a") as file:
        file.write(message + "\n")