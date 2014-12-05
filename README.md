WFTransactionGrabber
=================

A web driver to download account activity .qfx files from Wells Fargo (for YNAB). Written in Python using [Splinter](http://splinter.cobrateam.info/).

Build Instructions
------------------

#### Dependencies
This project uses Pants to build executable binaries. In addition, there are a number of python libraries that are used in the source, most notably Splinter.

It is recommended that virtualenv and pip be used to manage these dependencies. While in a virtualenv, running `./build_targets` will install all needed dependencies using pip, and build the project binaries in `bin/`.

Other Information
-----------------
* This project was created on Mac OS X Yosemite (10.10) and is completely untested on other platforms.

* Set Firefox to automatically save downloads for best results.
