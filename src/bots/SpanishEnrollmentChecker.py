#------------------------------ imports --------------------------------

# standard modules
from getpass import getpass

# intra-project modules
from browsers import MyREDBrowser

# external libraries
# N/A

#-----------------------------------------------------------------------


def main():
    """Checks MyRED to see if SPAN202-001 is open."""

    # get login details from terminal
    username = raw_input('NUID: ')
    password = getpass('MyRED Password: ')

    # create a driver for Wells Fargo
    with MyREDBrowser() as browser:

        # go to wellsfargo.com and login
        browser.nav_home()
        browser.login(username, password)

        browser.nav_to_edit_enrollment()

        # pause for a few seconds
        browser.wait(20)


if __name__ == "__main__":
    main()
