


import time
t=time.strftime("%H:%M:%S")
hour=time.strftime("%H")
print(t)

if int(hour)>=6 and int(hour)<=12  :
    print("Good Morning")
elif int(hour)>12 and int(hour)<=18:
    print("Good Evening")
elif  int(hour)<=6:
    print("Good Night")
