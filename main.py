import audio_interface
import weather_getter
import re


if __name__ == "__main__":

    #print(weather_getter.get_weather('London'))

    input()

    while True:

        voice_input = audio_interface.record_and_recognize_audio(4)
        print(voice_input)

        try:
            city = re.search(r'in (\w)+', voice_input)[0].split(' ')[1].title()
        except:
            city = 'Novosibirsk'

        days = []
        try:
            if re.search(r'tomorrow', voice_input):
                days.append(1)
            if re.search(r'today', voice_input):
                days.append(0)
        except:
            pass

        if len(days) == 0:
            days = [0]

        try:
            print(weather_getter.get_weather(city, days))
        except Exception as e:
            print('error', e)

