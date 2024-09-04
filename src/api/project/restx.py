import logging
from flask_restx import Api
from src.api.settings import envs
from src.api.project.constants import CodeHttp, Messages
from src.api.project.utils import objLogger, objResponse
from src.api.project.exception.NotTreatementError import NotTreatmentException


log = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Documentation",
    description="Documentation swagger.",
    doc="/doc",
)

objLogger.info(f"Running as {envs.ENVIRONMENT}.")


@api.errorhandler
def default_error_handler(e):
    objLogger.error(Messages.ERROR.NOT_TREATMENT)

    if not envs.FLASK_DEBUG:
        return objResponse.send_exception(
            NotTreatmentException, Messages.ERROR.NOT_TREATMENT, CodeHttp.ERROR.INTERNAL_ERROR
        )
