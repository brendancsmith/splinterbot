#------------------------------ imports --------------------------------

# standard modules
import time

from collections import namedtuple
from getpass import getpass

# intra-project modules
from plugins import PluginReceiver

# external libraries
# N/A

#-----------------------------------------------------------------------


class Bot(PluginReceiver, object):

    @staticmethod
    def wait(self, sec=5):
        time.sleep(sec)


class LoginManager(dict):

    Login = namedtuple('Login', ['username', 'password'])

    @staticmethod
    def ask(userLabel='Username', passLabel='Password'):
        username = raw_input(userLabel + ': ')
        password = getpass(passLabel + ': ')
        return LoginManager.Login(username, password)

    def __setitem__(self, key, value):
        if isinstance(value, LoginManager.Login):
            return super(LoginManager, self).__setitem__(key, value)

        else:
            try:
                assert len(value) == 2
            except (TypeError, AssertionError):
                pass
            else:
                login = LoginManager.Login(*value)
                return super(LoginManager, self).__setitem__(key, login)

        raise TypeError('Not a recognized username/password pair.')
