#------------------------------ imports --------------------------------

# standard modules
import smtplib

# intra-project modules
# N/A

# external libraries
# N/A

#-----------------------------------------------------------------------


class GmailServer(smtplib.SMTP, object):

    # NOTE: Login will not work if you are using two-factor authentication.
    #       An application-specific password is required.

    def __init__(self, username, password):
        super(GmailServer, self).__init__('smtp.gmail.com:587')
        self.starttls()
        self.login(username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()


def send_email(gmailAddr, gmailPassword, msg):
        with GmailServer(gmailAddr, gmailPassword) as mailServer:
            mailServer.sendmail(gmailAddr, [gmailAddr], msg)
