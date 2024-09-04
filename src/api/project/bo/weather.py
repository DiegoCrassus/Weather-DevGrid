import asyncio
import aiohttp
import threading
from flask import current_app
from src.api.extensions import db
from src.api.settings import envs
from src.api.project.utils import BasicVars, objLogger
from src.api.project.schema import WeatherData
from src.api.project.repository import DatabaseOperations


db_operations = DatabaseOperations(db)


class WeatherBO:
    def __init__(self):
        self.collected_data_by_user = {}

    async def send_request(self, session, url, user_id):
        async with session.get(url) as response:
            response = await response.json()

            try:
                new_weather = WeatherData(
                    user_id=user_id,
                    lon=response['coord']['lon'],
                    lat=response['coord']['lat'],
                    weather_id=response['weather'][0]['id'],
                    weather_main=response['weather'][0]['main'],
                    weather_description=response['weather'][0]['description'],
                    weather_icon=response['weather'][0]['icon'],
                    temp=response['main']['temp'],
                    feels_like=response['main']['feels_like'],
                    temp_min=response['main']['temp_min'],
                    temp_max=response['main']['temp_max'],
                    pressure=response['main']['pressure'],
                    humidity=response['main']['humidity'],
                    sea_level=response.get('sea_level'),
                    grnd_level=response.get('grnd_level'),
                    visibility=response.get('visibility', 10000),
                    wind_speed=response['wind']['speed'],
                    wind_deg=response['wind']['deg'],
                    wind_gust=response['wind'].get('gust', 0.0),
                    clouds_all=response['clouds']['all'],
                    dt=response['dt'],
                    sys_country=response['sys']['country'],
                    sys_sunrise=response['sys']['sunrise'],
                    sys_sunset=response['sys']['sunset'],
                    timezone=response['timezone'],
                    city_id=response['id'],
                    city_name=response['name'],
                    cod=response['cod']
                )
                db_operations.insert_weather_data(new_weather)
                self.collected_data_by_user[user_id] += 1

            except KeyError as e:
                print(f"Missing expected data in response: {str(e)}")
            except Exception as e:
                print(f"Unexpected error occurred: {str(e)}")

        await asyncio.sleep(2)

    async def handle_requests(self, url, user_id):
        async with aiohttp.ClientSession() as session:
            tasks = []
            cities_code = BasicVars.CITIES_ID_MOCK if current_app.testing else BasicVars.CITIES_ID
            for city_id in cities_code:
                formatted_url = url.format(city_id, envs.OPEN_WEATHER_KEY)
                task = asyncio.create_task(self.send_request(session, formatted_url, user_id))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def handler(self, req):
        user_id = req["user_id"]
        self.collected_data_by_user[user_id] = 0
        url = envs.OPEN_WEATHER_URL
        app = current_app._get_current_object()

        def background_task(app):
            with app.app_context():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.handle_requests(url, user_id))
                loop.close()

        try:
            objLogger.info(f"Starting request cities weather for user: {user_id}")
            thread = threading.Thread(target=background_task, args=(app,))
            thread.start()
            return "Requests initiated successfully"
        except Exception as e:
            objLogger.error(f"Failed to initiate weather requests: {str(e)}")
            return str(e)
        
    def get_user_collect_data(self, user_id):
        return round(self.collected_data_by_user[str(user_id)] / len(BasicVars.CITIES_ID), 3) * 100 if str(user_id) in self.collected_data_by_user else 0
