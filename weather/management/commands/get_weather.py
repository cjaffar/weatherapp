import requests
from datetime                       import datetime
from django.core.management.base    import BaseCommand, CommandError
from django.conf                    import settings

from weather.models import City, Weather

class Command(BaseCommand):
    help = 'Get weather info from openweathermap'

    def add_arguments(self, parser):
        parser.add_argument(
            'cityid',
            type=int
        )

    def handle(self, *args, **options):

        api_key = settings.OPENWEATHER_API_KEY
        cityid = options['cityid']

        url = 'https://api.openweathermap.org/data/2.5/onecall'
        params = { 'exclude' : 'hourly,current', 'appid': api_key }

        city = City.active.all().order_by('?') #filter(cityid=cityid).first()
        city = city.first()

        if not city :
            self.stdout.write(self.style.ERROR('City ID not found or CityID is not in South Africa'))
            return

        coords = city.coord
        params['lat'] = coords.get('latitude')
        params['lon'] = coords.get('longitude')

        req = requests.get(url, params=params)
        if req.status_code != 200 :
            self.stdout.write(self.style.ERROR('Request returned an error: (%s) %s') % (req.status_code, req.text))
            return

        resp = req.json()
        daily_data = resp.get('daily', [])
        if not daily_data :
            self.stdout.write(self.style.ERROR('Request returned an error: (%s) %s') % (req.status_code, req.text))
            return

        for data in daily_data :

            for key, d in data.items() :
                print('%s => %s' % (key,d))

            date = datetime.fromtimestamp(data.get('dt'))
            temp = data.get('temp')
            wind_speed = data.get('wind_speed')
            rain = '-'
            weather = data.get('weather')

            if data.get('rain') is not None :

                for w in data.get('weather', []) :
                    if w.get('main') == 'Rain' :
                        rain = w.get('description')
                        break

            w_model = Weather.objects.filter(date=date, city = city).first()
            if not w_model :
                w_model = Weather(date=date, city=city)

            w_model.rain=rain
            w_model.weather=weather
            w_model.wind_speed=wind_speed
            w_model.max_temp=temp.get('max')
            w_model.min_temp=temp.get('min')

            w_model.save()

        return