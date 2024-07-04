import webview
from flask import Flask
from flask_session import Session

from examples.password_manager.src.routes.home import HomeRoute
from examples.password_manager.src.types import ConfigProtocol, ServerConfigProtocol
from examples.password_manager.src.socket import socketio


class PasswordManagerApp:
    def __init__(self, app_name: str, config: ConfigProtocol, server_config: ServerConfigProtocol):
        self._window = None
        self._app_name = app_name
        self._flask_app_name = __name__
        self._config = config
        self._server_config = server_config

        self._routes = [
            HomeRoute
        ]

        self._initialize_app()
        self._initialize_window()

    def _initialize_app(self):
        self._app = Flask(self._flask_app_name, template_folder=self._server_config.TEMPLATE_FOLDER,
                          static_folder=self._server_config.STATIC_FOLDER)
        self._app.debug = False
        self._app.config.from_object(self._config)
        socketio.init_app(self._app, async_mode="threading")

        Session(self._app)

        self._configure_routes()

    def _initialize_window(self):
        self._window = webview.create_window(
            self._app_name,
            f"http://{self._server_config.HOST}:{self._server_config.PORT}",
            width=800,
            height=600,
            resizable=False,
            maximized=False
        )

    def _run_socketio(self):
        socketio.run(app=self._app, host=self._server_config.HOST, port=self._server_config.PORT,
                     allow_unsafe_werkzeug=True)

    def _configure_routes(self):
        for route in self._routes:
            self._app.add_url_rule(
                route.route_path,
                view_func=route.as_view(route.route_name)
            )

    def run_app(self):
        webview.start(self._run_socketio, ())
