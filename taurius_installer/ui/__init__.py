import webview
from flask import Flask

from taurius_installer.ui.conf.constants import Constants
from taurius_installer.socket import socketio


class TauriusUpdater:
    def __init__(self, host: str = None, port: int = None, url: str = None, app_name: str = "Taurius Updater"):
        self._host = host
        self._port = port
        self._url = url
        self._app_name = app_name

        self._main_window = None
        self._app = None

    def initialize(self):
        title = self._app_name
        if self._url is None and self._host is None:
            url_to_open = f"http://{Constants.HOST}:{Constants.PORT}"

            self._host = Constants.HOST
            self._port = Constants.PORT
        elif self._url is not None:
            url_to_open = self._url
            parts = url_to_open.replace("http://", "").split(":")

            self._host = parts[0]
            self._port = int(parts[1])
        else:
            url_to_open = f"http://{self._host}:{self._port}"

        self._app = self._initialize_flask()
        self._main_window = webview.create_window(title, url_to_open, maximized=False)
        webview.start(self._initialize_socket, (self._app, self._host, self._port))

    @staticmethod
    def _initialize_socket(app, host, port):
        socketio.run(app=app, host=host, port=port, allow_unsafe_werkzeug=True)

    @staticmethod
    def _initialize_flask():
        app = Flask(__name__)
        socketio.init_app(app, async_mode="threading")

        return app

