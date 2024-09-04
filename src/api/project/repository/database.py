from src.api.extensions import db
from src.api.project.schema import Users, WeatherData
from tests.test_case.test_validator import mock_if_testing


class DatabaseOperations:
    def __init__(self, db_session=None):
        self.db = db_session or db

    @mock_if_testing
    def insert_user(self, username: str):
        try:
            new_user = Users(username=username)
            self.db.session.add(new_user)
            self.db.session.commit()
            return new_user
        except Exception as error:
            self.db.session.rollback()
            raise error

    @mock_if_testing
    def select_user(self, user_id: str):
        try:
            user = Users.query.get(user_id)
            return user
        except Exception as error:
            raise error

    @mock_if_testing  
    def select_all_users(self):
        try:
            users = Users.query.all()
            return users
        except Exception as error:
            raise error
        
    @mock_if_testing
    def insert_weather_data(self, new_weather: WeatherData):
        try:
            self.db.session.add(new_weather)
            self.db.session.commit()
            return new_weather
        except Exception as error:
            self.db.session.rollback()
            raise error

    @mock_if_testing
    def select_weather(self, user_id: str):
        try:
            weather = WeatherData.query.get(user_id)
            return weather
        except Exception as error:
            raise error
