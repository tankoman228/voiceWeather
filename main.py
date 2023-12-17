import datetime

import audio_interface
import commands

import re

days_of_week = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
}

if __name__ == "__main__":

    while True:

        weather_query_like = 0

        voice_input = audio_interface.record_and_recognize_audio(4)
        #voice_input = input('cmd: ')
        print(voice_input)

        try:
            city = re.search(r'in (\w)+', voice_input)[0].split(' ')[1].title()
            weather_query_like += 1
        except:
            city = commands.get_city()

        try:

            split_cmd = voice_input.split(' ')
            command = voice_input.replace(' ' + split_cmd[len(split_cmd) - 1], '')

            if command in commands.commands:
                commands.commands[command](split_cmd[len(split_cmd) - 1])
                continue

            days = []
            if re.search(r'today', voice_input):
                days.append(0)
                weather_query_like += 1
            if re.search(r'tomorrow', voice_input):
                days.append(1)
                weather_query_like += 1

            words = voice_input.split(' ')
            for word in words:
                if word in days_of_week.keys():
                    day_of_week = days_of_week[word]
                    days_to_next_day_of_week = (datetime.date.today().weekday() - day_of_week)
                    days.append(days_to_next_day_of_week)
                    print(days_to_next_day_of_week)

            if len(days) == 0:
                days = [0]

            if re.search(r'weather', voice_input):
                weather_query_like += 1
            elif re.search(r'forecast', voice_input):
                weather_query_like += 1
            elif re.search(r'will be', voice_input):
                weather_query_like += 1
            elif re.search(r'is', voice_input):
                weather_query_like += 1

            if weather_query_like > 0:

                weather = commands.get_weather(city, days)
                text = ''
                for day in weather:
                    c = day[1]
                    text += f'at {day[0].split(".")[0]} in {city} will be {day[2]}, temperature about {int(c["temp"])} '
                # print(text)
                audio_interface.play_voice_assistant_speech(text)

        except Exception as e:
            print('error', e)
