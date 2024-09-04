from src.api.app import app
from src.api.settings import envs


def start():
    print(__package__, " started.")
    app.run(host=envs.FLASK_HOST, port=envs.FLASK_PORT, debug=envs.FLASK_DEBUG)


if __name__ == "__main__":
    start()
