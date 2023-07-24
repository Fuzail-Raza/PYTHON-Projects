import time
import os
import winsound
from win10toast import ToastNotifier
# import notify2 #For Cross platforms
time_start=time.strftime("%H")
while True:
    time_now=int(time.strftime("%H"))-int(time_start)
    if(time_now>10):
        # notify2.init("Notification App")
        # notification = notify2.Notification("Take Rest", f"Please Take a rest for while you are using laptop for {time_now} Hours with no break")
        # notification.show()
        toaster = ToastNotifier()
        toaster.show_toast("Take Rest", f"Please Take a rest for while you are using laptop for {time_now} Hours with no break", duration=1)
        frequency = 1000  
        duration = 1000
        winsound.Beep(frequency, duration)
        break