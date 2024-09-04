import logging
import traceback
from src.api.settings import envs
from flask import request
from flask_restx import Resource
from src.api.project.restx import api
from src.api.project.constants import CodeHttp, Messages
from src.api.project.utils import doc_swagger
from src.api.project.restx import objLogger, objResponse
from src.api.project.bo import weather_operation

log = logging.getLogger(__name__)
ns = api.namespace(envs.WEATHER_ENDPOINT, description="Weather operation.")


@ns.route(envs.ROUTE, methods=["POST"])
class WeatherPostResource(Resource):
    @api.expect(doc_swagger.INPUT_DATA)
    def post(self):
        objLogger.debug(Messages.REQUEST_RECEIVED)
        request_data = request.get_json()

        try:
            data = weather_operation.handler(request_data)
            response = objResponse.send_success(
                messages=Messages.SUCCESS.DONE, status=CodeHttp.SUCCESS.OK, data=data
            )
            objLogger.success(messages=Messages.SUCCESS.DONE)

        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Messages.ERROR.BUSINESS, status=CodeHttp.ERROR.INTERNAL_ERROR
            )
            objLogger.error(messages=Messages.ERROR.BUSINESS)
            objLogger.debug(messages=traceback.format_exc())

        return response

@ns.route(envs.ROUTE + '<int:user_id>', methods=["GET"])
class WeatherGetResource(Resource):
    def get(self, user_id):
        objLogger.debug(f"Processing request for user_id: {user_id}")
        try:
            percentage = weather_operation.get_user_collect_data(user_id)
            data = f"Processed: {percentage}%"
            response = objResponse.send_success(
                messages=Messages.SUCCESS.DONE, status=CodeHttp.SUCCESS.OK, data=data
            )
            objLogger.success(messages=Messages.SUCCESS.DONE)

        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Messages.ERROR.BUSINESS, status=CodeHttp.ERROR.INTERNAL_ERROR
            )
            objLogger.error(messages=Messages.ERROR.BUSINESS)
            objLogger.debug(messages=traceback.format_exc())

        return response
