
import requests
import json
import win32com.client

def weather():
    try:
        city=input("Enter Your City")
        url=f"http://api.weatherapi.com/v1/current.json?key=7e76bbb4196f47ad940193323232807&q={city}"

        respone=requests.get(url)
        wdict=json.loads(respone.text)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Voice =  speaker.GetVoices().Item(1)
        print(f"The weather of {city} is {wdict['current']['temp_c']}C and Wind Speed is  {wdict['current']['wind_mph']}")
        speaker.Speak(f"The weather of {city} is {wdict['current']['temp_c']}Celsius and Wind Speed is  {wdict['current']['wind_mph']}")
    except :
        print("City Entered Incorrectly")
        weather()
    while True:
        choice=int(input("Enter 1 for full details and 0 to exit"))
        if(choice==1):
            speaker.Speak("Here are the full details : ")

            for key, value in wdict.items():
                print(value)
                speaker.Speak(value)
            break
        elif choice==0 :
            print("See u in Next Rain")
            speaker.Speak("See u in Next Rain")
            break
        else:
            print("Incorrect Option")
            speaker.Speak("Incorrect Option")


if __name__=="__main__":
    weather()