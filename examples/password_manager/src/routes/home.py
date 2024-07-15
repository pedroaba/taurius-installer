import os
import json

from flask import render_template

from examples.password_manager.src.routes.base import BaseRoute


class HomeRoute(BaseRoute):
    route_name = "home"
    route_path = "/"

    methods = ["GET"]

    def get(self):
        context = self.get_base_context()

        passwords = {}
        if os.path.exists('password.json'):
            with open('password.json', 'r') as f:
                passwords = json.load(f)
        context["passwords"] = ",".join(list(
            passwords.keys()
        ))

        return render_template("home/index.html", context=context)
