import pyttsx3
vtf = pyttsx3.init()

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate
vtf.setProperty('rate', 140)     # setting up new voice rate

def vtf_speak(text):
    print('speaking.....')
    vtf.say(text)
    vtf.runAndWait()

txt = "Hey friend, I am your virtual talking friend"
vtf_speak(txt)

while txt != 'bye':
    txt = input("what should I say : ")
    txt = txt.lower()
    if txt != 'bye':
        vtf_speak(txt)
    else:
        vtf_speak('see you again friend,that was nice talking to you')
