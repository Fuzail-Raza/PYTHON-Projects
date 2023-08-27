
import string
import random

samples=[]
samples.extend(string.ascii_lowercase)
samples.extend(string.ascii_uppercase)
samples.extend(string.punctuation)
samples.extend(string.digits)

while True:
    try:
        plen=int(input("Enter Lenght of Password"))
        break
    except :
        print("Invalid Input")

random.shuffle(samples)


password="".join(samples[0:plen])

print(password)    