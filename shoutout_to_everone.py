

import win32com.client
names=["Fuzail","Raza","Attari"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice =  speaker.GetVoices().Item(1)
for name in names:
    print(name)
    speaker.Speak(name)
# Create a SAPI SpVoice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Get the list of available voices
voices = speaker.GetVoices()

# Print the names of all available voices
for voice in voices:
    print(voice.GetDescription())