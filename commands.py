import audio_interface
import weather_getter


def get_weather(city, days=[0, 1]):
    return weather_getter.get_weather(city, days)


def set_city(city):
    weather_getter.current_city = city
    audio_interface.play_voice_assistant_speech('your city is set to ' + weather_getter.current_city)


def get_city():
    return weather_getter.current_city


commands = {
    "set current city": set_city,
    "set city": set_city,
    "city": set_city
}
