import speech_recognition as sr
from sentiment import startAnalysis
from csvWriter import writer
import time
import datetime
def record(filenames):
    for file in filenames:
        r = sr.Recognizer()
        with sr.WavFile(file) as source:              # use "test.wav" as the audio source
            audio = r.record(source)                        # extract audio data from the file

        try:
            transcription= r.recognize_google(audio)
            ts=time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')   # recognize speech using Google Speech Recognition
            writer([[transcription]],'{}.csv'.format(st))
        except LookupError:                                 # speech is unintelligible
            print("Could not understand audio")
    startAnalysis('{}.csv'.format(st))
    

