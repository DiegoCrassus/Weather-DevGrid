from src.api.project.constants import Message


class NotTreatmentException(Exception):
    def __init__(self, msg):
        super().__init__(Message.ERROR_NOT_TREATMENT)
