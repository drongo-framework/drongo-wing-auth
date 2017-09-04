from ._activation_code import ActivationCode
from ._login_attempts import LoginAttempt
from ._users import User

import uuid


class MongoBackend(object):
    def __init__(self, config):
        self.config = config
        self.modules = config.modules

        self.users = User(self.config)
        self.activation_codes = ActivationCode(self.config)
        self.login_attempts = LoginAttempt(self.config)

    def init(self):
        self.users.init()
        self.activation_codes.init()
        self.login_attempts.init()

    def check_user_exists(self, username):
        return self.users.check_exists(username)

    def create_user(self, username, password, active=False):
        self.users.create(username, password, active)

    def login(self, ctx, username, password):
        return self.users.verify_login(username, password)

    def logout(self, ctx):
        pass

    def activate(self, username, code):
        pass