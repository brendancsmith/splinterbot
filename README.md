WFTransactionGrabber
=================

A web driver to download account activity .qfx files from Wells Fargo (for YNAB). Written in Python using [Splinter](http://splinter.cobrateam.info/) and built using Twitter's [Pants](https://pantsbuild.github.io/).


Build Instructions
------------------

This project requires [pip](https://pypi.python.org/pypi/pip) for dependency management. [virtualenv](http://virtualenv.readthedocs.org/en/latest/) is also recommended. These are very common python development tools.

1.  Install Pants etc. using pip.

    ```{bash}
    pip install -r requirements.txt
    ```

1.  Build the bot executables using Pants. The `.pex` executables will be created in the `dist/` directory.

    ```{bash}
    pants src/bots:
    ```

Alternatively, running `./build_bots` build with Pants and create simple executables in the `bin/` directory.


Other Information
-----------------
* This project was created on Mac OS X Yosemite (10.10) and is completely untested on other platforms.

* Set Firefox to automatically save downloads for best results.
