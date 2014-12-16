#------------------------------ imports --------------------------------

# standard modules
# N/A

# intra-project modules
from splinterbot.browsers import WFBrowser
from splinterbot.bot import Bot

# external libraries
# N/A

#-----------------------------------------------------------------------


class TransactionDownloader(Bot):

    def run(self):
        """Downloads all account exports with the input account info."""

        # get login details from terminal
        username, password = self.ask_login_details('Wells Fargo Login',
                                                    'username', 'password')

        # create a driver for Wells Fargo
        with WFBrowser() as browser:

            # go to wellsfargo.com and login
            browser.nav_home()
            browser.login(username, password)

            # go to the download activity page,
            # and download the account exports
            browser.nav_to_download_page()
            browser.download_all_accounts()

            # give some extra time in case Firefox makes download alerts
            self.wait()


if __name__ == "__main__":
    TransactionDownloader().run()
