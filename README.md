# Auto_login for IIT Bombay
This is a small code snippet, for automatic login in internet.iitb.ac.in for guys staying in IIT Bombay. This code can be modified and used for many such logins. There are two python files listed above, namely:
* auto_login_ldap.py
* auto_login_ldap_phantom.py

auto_login_ldap,py uses chrome browser, i.e. a chrome browser will pop up and it will autologin and browser will close. It happens in a span of 3 secs.

auto_login_ldap_phantom.py uses PhantomJS. Here no browser will pop up, It will just show the status in the terminal. If the user is not logged in, then it will automatically login the user.

## Dependencies

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Selenium python library](https://pypi.python.org/pypi/selenium)
* PhantomJS (If you use auto_login_ldap_phantom.py)
* [Chrome Webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

I am against using PhantomJS with python, but anyway I added a line, so anyone can use it. The easiest way to use PhantomJS in python is via Selenium. The simplest installation method is

* Install NodeJS
* Using Node's package manager install phantomjs: `npm -g install phantomjs-prebuilt`
* install selenium (in your virtualenv, if you are using that)

To know more about it check [this link](https://dzone.com/articles/python-testing-phantomjs)
You can use, any other webdriver like firefox webdriver, or your choice of webdriver.


## How to use
Create a file in which you will keep your LDAP username and the LDAP password, each in differnt lines. A sample 'key' file is already provided. For fast implementation keep the file in the same directory as your .py file. Just run the code from the terminal.

```python
$python auto_login_ldap.py key
```

This is done to keep your password safe in a different file. But you can put your password directly in the code for testing, but that won't be so much secured.

## Another way of using the script:


* In the python code, include both the username and the password.
* Create a compiled version - auto_login_ldap.pyc - by importing this module via python command line.
* Now remove the username and password from your original code.
* Now run the compiled code.

Since auto_login_ldap.pyc is byte compiled it is not readable to the casual user. This is be a bit more secure than hardcoding credentials, although it is vulnerable to a py_to_pyc decompiler.
I generally use this way of running the script. Though it is not at all safe, but it still pretty much serves the purpose of fast implementaion.
