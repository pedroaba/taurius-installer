import json
import os.path

from flask import request, flash, redirect

from examples.password_manager.src.routes.base import BaseRoute


class PasswordManagerRoute(BaseRoute):
    route_name = 'password_manager'
    route_path = '/password'

    methods = ['POST']

    @staticmethod
    def save_password(name, password):
        passwords = {}

        if os.path.exists('password.json'):
            with open('password.json', 'r') as f:
                passwords = json.load(f)

        # Caesar cipher
        hashed_password = ""
        for char in password:
            # Encrypt uppercase characters
            if char.isupper():
                hashed_password += chr((ord(char) + 4 - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                hashed_password += chr((ord(char) + 4 - 97) % 26 + 97)

        with open('password.json', 'w') as f:
            passwords.update({name: hashed_password})
            json.dump(passwords, f)

    def post(self):
        password_name = request.form.get('password-name', None)
        password = request.form.get('password', None)

        if not password_name or not password:
            flash('Invalid forms')
            return redirect('/')

        self.save_password(password_name, password)

        flash('Password was saved successfully')
        return redirect('/')
