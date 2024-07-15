from typing import TypedDict

from flask.views import MethodView


class BaseContext(TypedDict):
    title: str


class BaseRoute(MethodView):
    route_name: str = "route"
    route_path: str = "/route"

    def __init__(self, *args, **kwargs):
        super(BaseRoute, self).__init__(*args, **kwargs)

    def get_base_context(self) -> BaseContext:
        return {
            "title": "Password Manager Home"
        }
