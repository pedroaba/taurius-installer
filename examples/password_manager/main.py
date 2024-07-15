from examples.password_manager.src.settings import ServerConfig, Config
from examples.password_manager.src import PasswordManagerApp

if __name__ == "__main__":
    application = PasswordManagerApp(
        "PasswordManagerApp", Config, ServerConfig
    )

    application.run_app()
