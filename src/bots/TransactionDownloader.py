"""
TransactionDownloader

Usage:
    TransactionDownloader
    TransactionDownloader -h | --help

Options:
    -h --help    Show this sceen.

"""

#------------------------------ imports --------------------------------

# standard modules
from docopt import docopt

# intra-project modules
from sites.wells_fargo import WFBrowser
from splinterbot.bot import Bot, LoginManager

# external libraries
# N/A

#-----------------------------------------------------------------------


class TransactionDownloader(Bot):

    def __init__(self):
        self.logins = LoginManager()

    def run(self):
        """Downloads all account exports with the input account info."""

        # get login details from terminal
        self.logins['wells_fargo'] = LoginManager.ask('Wells Fargo Username',
                                                      'Wells Fargo Password')

        # create a driver for Wells Fargo
        with WFBrowser() as browser:

            # go to wellsfargo.com and login
            browser.nav_home()
            browser.login(*self.logins['wells_fargo'])

            # go to the download activity page,
            # and download the account exports
            browser.nav_to_download_page()
            browser.download_all_accounts()

            # give some extra time in case Firefox makes download alerts
            self.wait()


if __name__ == "__main__":
    args = docopt(__doc__)
    TransactionDownloader().run()
