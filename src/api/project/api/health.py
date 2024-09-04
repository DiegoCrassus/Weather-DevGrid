from flask_restx import Resource
from src.api.project.restx import api
from src.api.settings import envs

ns = api.namespace(envs.HEALTH_ENDPOINT, description="Health operation")


@ns.route("")
class LiveCollection(Resource):
    def get(self):
        return f"Running version: {envs.VERSION}", 200
