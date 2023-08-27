import time 
from player import notification

if __name__=="__main":
    notification.notify (
        title="Take a Break",
        message="Take a break for 10 minutes",
        app_icon="PATH",
        timeout=10
    )