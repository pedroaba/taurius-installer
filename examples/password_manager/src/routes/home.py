from flask import render_template

from examples.password_manager.src.routes.base import BaseRoute


class HomeRoute(BaseRoute):
    route_name = "home"
    route_path = "/"

    methods = ["GET"]

    def get(self):
        context = self.get_base_context()

        return render_template("home/index.html", context=context)
