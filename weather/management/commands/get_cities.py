import os, json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from weather.models import City

class Command(BaseCommand):
    help = 'Get list of South African cities from Openweather'

    def handle(self, *args, **options):
        """"
        JSON file from openweathermap is stored at resources folder. This is then read through in order to input into the DB.
        """
        resource_file = settings.BASE_DIR / 'resources' / 'city.list.json'
        cities = {}
        if os.path.isfile(resource_file) :
            with open(resource_file, 'r') as resource :
                cities = json.load(resource)

        if not cities:
            self.stdout.write(self.style.ERROR('Zero list of cities from weathermap OR city file not found.'))
            return

        count = 0
        for city in cities:
            if city.get('country') == 'ZA':

                w_city = City.objects.filter(cityid = city.get('id', '-999')).first()
                if not w_city :
                    w_city = City(cityid=city.get('id', '-999'))

                city_coords = city.get('coord', {})

                coords = { 'latitude' : city_coords.get('lat', 0), 'longitude' : city_coords.get('lon', 0)}
                w_city.name = city.get('name', 'N/A')
                w_city.country = city.get('country')
                w_city.coord = coords
                w_city.save()

                count += 1

        self.stdout.write(self.style.SUCCESS('Total number of cities pulled: %d ' % count))
        return