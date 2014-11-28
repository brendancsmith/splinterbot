from browsers import WFBrowser


def main():
    browser = WFBrowser()
    browser.visit('http://wellsfargo.com')

    browser.login('foo', 'bar')

    # Just for demo/debugging.
    import time
    time.sleep(5)

    browser.quit()


if __name__ == "__main__":
    main()
