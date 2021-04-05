# weatherapp

1. Checkout branch 'master'
2. copy deviare/settings_local.py.example to deviare/settings_local.py
3. change db credentials in settings_local.py (uses postgresql)
4. do django housekeeping stuff // pip install, make migration, createsuperuser, etc.
5. run command get_cities in order to download cities from owm
6. get_weather command gets weather forecast for one city -- use cityid
7. run.