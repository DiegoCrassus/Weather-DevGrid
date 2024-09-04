from flask_restx import fields
from src.api.project.restx import api

# expected input values of api
INPUT_DATA = api.model(
    "input",
    {
        "user_id": fields.String(
            required=True, description="User id", example="1"
        )
    },
)

OUTPUT_DATA = api.model(
    "Output",
    {
        "messages": fields.String(required=True, description="Sucess or Error mensage"),
        "status": fields.String(required=True, description="Status code"),
        "data": fields.Raw(required=False, description="response"),
    },
)
