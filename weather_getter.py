from pyowm import OWM
from datetime import datetime, timedelta

current_city = 'Novosibirsk'


def get_weather(city, days=[0, 1]):
    owm = OWM('8445d2132b489929791428e7895e3a48')
    weather_manager = owm.weather_manager()

    result = []
    for day in days:
        date = datetime.now() + timedelta(days=day) + timedelta(hours=2)
        forecast = weather_manager.forecast_at_place(current_city, '3h')
        w = forecast.get_weather_at(date)
        temp = w.temperature('celsius')
        weather = w.detailed_status
        result.append([date.strftime("%d.%m.%Y"), temp, weather])

    return result