import pyttsx3  # синтез речи (Text-To-Speech)
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)


# Init AI voice
def setup_assistant_voice():
    voices = ttsEngine.getProperty("voices")
    ttsEngine.setProperty("voice", voices[1].id)


# Text to speech
def play_voice_assistant_speech(text_to_speech: str):
    print('bot: ', text_to_speech)
    ttsEngine.say(text_to_speech)
    ttsEngine.runAndWait()


# Speech to text
def record_and_recognize_audio(await_time: int):
    with microphone:
        recognized_data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, await_time, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="eng").lower()

        except speech_recognition.UnknownValueError:
            return

        except speech_recognition.RequestError:
            print("offline: error")
            return

        return recognized_data


recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

ttsEngine = pyttsx3.init()
setup_assistant_voice()
