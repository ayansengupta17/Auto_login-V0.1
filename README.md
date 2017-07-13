# auto_login
This is a small code snippet, for auto login for guys staying in IIT Bombay.

##Dependencies

* Python 2.7
* Selenium python library
* PhantomJS (optional)
* Chrome Webdriver

I am against using PhantomJS with python, but anyway I added a line, so anyone can use it. The easiest way to use PhantomJS in python is via Selenium. The simplest installation method is

* Install NodeJS
* Using Node's package manager install phantomjs: npm -g install phantomjs-prebuilt
* install selenium (in your virtualenv, if you are using that)

You can use, any other webdriver like firefox webdriver.


## How to use
Create a file in which you will keep your LDAP username and the LDAP password, each in differnt lines. A sample 'key' file is already provided. Just run the code from the terminal.

'''python
python auto_login_ldap.py key
'''

This is done to keep your password safe in a different file. But you can put your password directly in the code for testing, but that won't be so much secured.


