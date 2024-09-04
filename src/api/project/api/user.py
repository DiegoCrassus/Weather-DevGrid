import logging
import traceback

from flask_restx import Resource
from src.api.settings import envs
from src.api.extensions import db
from src.api.project.restx import api
from src.api.project.constants import CodeHttp, Messages
from src.api.project.restx import objLogger, objResponse
from src.api.project.repository import DatabaseOperations

log = logging.getLogger(__name__)
ns = api.namespace(envs.USER_ENDPOINT, description="User operations")
db_operations = DatabaseOperations(db)

@ns.route('/add_user/<username>')
class AddUserResource(Resource):
    def get(self, username):
        try:
            user = db_operations.insert_user(username)
            data = f'User {user.username} added with ID {user.id}'

        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Messages.ERROR.BUSINESS, status=CodeHttp.ERROR.INTERNAL_ERROR
            )
            objLogger.error(messages=Messages.ERROR.BUSINESS)
            objLogger.debug(messages=traceback.format_exc())

        else:
            response = objResponse.send_success(
                messages=Messages.SUCCESS.DONE, status=CodeHttp.SUCCESS.OK, data=data
            )
            objLogger.success(messages=Messages.SUCCESS.DONE)

        return response

@ns.route('/get_user/<int:user_id>')
class GetUserResource(Resource):
    def get(self, user_id):
        try:
            user = db_operations.select_user(user_id)
            data = f'User ID: {user.id}, Username: {user.username}'

        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Messages.ERROR.BUSINESS, status=CodeHttp.ERROR.INTERNAL_ERROR
            )
            objLogger.error(messages=Messages.ERROR.BUSINESS)
            objLogger.debug(messages=traceback.format_exc())

        else:
            response = objResponse.send_success(
                messages=Messages.SUCCESS.DONE, status=CodeHttp.SUCCESS.OK, data=data
            )
            objLogger.success(messages=Messages.SUCCESS.DONE)

        return response

@ns.route('/get_all_users')
class GetAllUsersResource(Resource):
    def get(self):
        try:
            users = db_operations.select_all_users()
            data = [{'id': user.id, 'username': user.username} for user in users]
            
        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Messages.ERROR.BUSINESS, status=CodeHttp.ERROR.INTERNAL_ERROR
            )
            objLogger.error(messages=Messages.ERROR.BUSINESS)
            objLogger.debug(messages=traceback.format_exc())

        else:
            response = objResponse.send_success(
                messages=Messages.SUCCESS.DONE, status=CodeHttp.SUCCESS.OK, data=data
            )
            objLogger.success(messages=Messages.SUCCESS.DONE)

        return response