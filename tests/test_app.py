import json
import unittest
from unittest.mock import patch, MagicMock
from src.api.app import app as weather_app
from src.api.project.schema import Users, WeatherData


class TestUser(unittest.TestCase):
    def setUp(self):
        weather_app.testing = True
        self.app = weather_app.test_client()

        self.app_context = weather_app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get(self):
        response = self.app.get("/api/status")
        assert response.status_code == 200

    @patch('src.api.project.repository.DatabaseOperations.insert_user')
    def test_add_user_success(self, mock_insert_user):
        mock_user = MagicMock(spec=Users)
        mock_user.id = 1
        mock_user.username = "Test"
        mock_insert_user.return_value = mock_user

        new_user = "Test"
        response = self.app.get(f"/api/user/add_user/{new_user}")
        expected_response = {
            "data": "User Test added with ID 1",
            "messages": "Success: Done.",
            "status": "200"
        }
        print(response)
        assert (
            response.status_code == 200
            and json.loads(response.data)["data"] == expected_response["data"]
        )

    @patch('src.api.project.repository.DatabaseOperations.insert_user')
    def test_add_user_fail(self, mock_insert_user):
        mock_user = MagicMock(spec=Users)
        mock_user.id = 1
        mock_user.username = "Test"
        mock_insert_user.return_value = mock_user

        response = self.app.get(f"/api/user/add_user/")
        assert (
            response.status_code == 404
        )

    @patch('src.api.project.repository.DatabaseOperations.select_user')
    def test_get_user_success(self, mock_select_user):
        mock_user = MagicMock(spec=Users)
        mock_user.id = 1
        mock_user.username = "test"
        mock_select_user.return_value = mock_user

        response = self.app.get(f"/api/user/get_user/1")
        expected_response = {
            "data": "User ID: 1, Username: test",
            "messages": "Success: Done.",
            "status": "200"
            }
        assert (
            response.status_code == 200
            and json.loads(response.data)["data"] == expected_response["data"]
        )


    @patch('src.api.project.repository.DatabaseOperations.select_all_users')
    def test_get_all_users_success(self, mock_select_all_users):
        mock_user = MagicMock(spec=Users)
        mock_user.id = [1, 2]
        mock_user.username = ["Test", "Victor"]
        mock_select_all_users.return_value = mock_user

        response = self.app.get(f"/api/user/get_all_users")

        assert (
            response.status_code == 200
        )

    

    @patch('src.api.project.repository.DatabaseOperations.insert_weather_data')
    def test_weather_process_user(self, mock_insert_weather_data):
        mock_user = MagicMock(spec=WeatherData)
        mock_user.id = 1
        mock_user.username = "Test"
        mock_insert_weather_data.return_value = mock_user
        response = self.app.post(f"/api/weather/", json={"user_id": "1"})
        expected_response = {
            "data": "Requests initiated successfully",
            "messages": "Success: Done.",
            "status": "200"
            }
        assert (
            response.status_code == 200
            and json.loads(response.data)["data"] == expected_response["data"]
        )

    def test_weather_get_user_percentage(self):
        response = self.app.get(f"/api/weather/1")
        print(response)

        
        assert (
            response.status_code == 200
        )