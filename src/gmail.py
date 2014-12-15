#------------------------------ imports --------------------------------

# standard modules
import smtplib

# intra-project modules
# N/A

# external libraries
# N/A

#-----------------------------------------------------------------------

# NOTE: Login will not work if you are using two-factor authentication.
#       An application-specific password is required.


class Gmail(smtplib.SMTP):

    def __init__(self, username, password):
        self = smtplib.SMTP('smtp.gmail.com:587')
        self.starttls()
        self.login(username, password)

    def __enter__(self):
        return self

    def __exit__(self):
        self.quit()
