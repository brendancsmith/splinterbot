#------------------------------ imports --------------------------------

# standard modules
from getpass import getpass

# intra-project modules
from browsers import WFBrowser

# external libraries
# N/A

#-----------------------------------------------------------------------


def main():
    # get login details
    username = raw_input('username: ')
    password = getpass('password: ')

    # create a driver for Wells Fargo
    with WFBrowser() as browser:
        browser.visit(browser.url)
        browser.login(username, password)

        browser.nav_to_download_page()

        # Just for demo/debugging.
        import time
        time.sleep(5)


if __name__ == "__main__":
    main()
