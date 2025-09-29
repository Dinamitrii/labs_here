import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()

audio_file = '/home/dinamitrii/PycharmProjects/labs_here/audio_to_text/data/art_of_war_01-02_sun_tzu_64kb.mp3'


# udioSegment.from_mp3(audio_file).export(audio_file, format='mp3')
# audio = AudioSegment.from_file(audio_file)

with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_bing(audio_data, language="bg", key="")
    print(text)
    print("Extracted Text:", text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("API Error:", e)

