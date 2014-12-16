#------------------------------ imports --------------------------------

# standard modules
import time

from getpass import getpass

# intra-project modules
# N/A

# external libraries
# N/A

#-----------------------------------------------------------------------


class Bot(object):

    @staticmethod
    def wait(self, sec=5):
        time.sleep(sec)

    def ask_login_details(self, loginTitle='Login:',
                          usernameLabel='Username', passwordLabel='Password'):
        print(loginTitle)
        print('=' * len(loginTitle))
        username = raw_input(usernameLabel + ': ')
        password = getpass(passwordLabel + ': ')

        return username, password