from typing import Protocol, Literal


class ConfigProtocol(Protocol):
    FLASK_DEBUG: int
    SESSION_FILE_DIR: int
    SESSION_PERMANENT: bool
    SESSION_TYPE: Literal["filesystem"]
    SECRET_KEY: str


class ServerConfigProtocol(Protocol):
    TEMPLATE_FOLDER: str
    STATIC_FOLDER: str

    HOST: str
    PORT: int
