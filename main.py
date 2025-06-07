from gtts import gTTS
import os

'''
    Using Mac os - 'say' command, to make simple robo speaker
    It does not support hindi
'''
def textToSpeech():
    while True:
        msg = input("Enter message: ")
        if msg == 'q':
            os.system("say 'bye bye friend'")
            break
        command = f'say {msg}'
        os.system(command)


'''
    Using google Text-to-Speech library (gTTS)
    It also support - hindi
    e.g. 
    msg = "how are you?"
    msg = "नमस्ते, आप कैसे हैं?"
'''

def textToSpeech2():
    while True:
        msg = input("Enter message: ")
        stop = False

        if msg == 'q':
            stop = True
            msg = 'okay bye, fir milte hai'

        tts = gTTS(text=msg, lang='hi')
        tts.save("output.mp3")
        os.system("afplay output.mp3")  # Works on Mac to play audio

        if stop == True:
            break;


print("Welcome to RoboSpeaker, Created by Rupesh!")
textToSpeech2()

