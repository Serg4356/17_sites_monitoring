# Sites Monitoring Utility

This script checks for sites status. For each url in url.txt script displays if server responds with HTTP 200 and information about expiration date.

### How to install

python has to be installed on your system. Use pip (or pip3 if there is conflict with Python 2) to install dependences.
```
pip install -r requirements.txt
```
It is recommended to use virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) to isolate your project 


### Quickstart

Programm provides a console interface. You can type -h to call interface description.

The interface has three main arguments:
'-u', '--url' - string argument - you can type 1 url directly from console.
'-p', '--path' - string argument - you can type path to txt file with url, which you want to check.
'-d', '--days' - integer argument - you can pecify number of days domain should be paid for. Default value is 30 days.

'-u' and '-p' arguments are mutually exclusive, so you must choose only one way to procceed.

For example you have file: urls.txt in your project folder, which looks like this:
```
http://wikipedia.org
http://coursera.com
http://roga.ikopyta
```
type into your console:
```
$python check_sites_health.py -p urls.txt -d 60
```
The output should look like this:
```
url: http://wikipedia.org
server response ok: True
domain expiration date: Domain name has been paid for more than 60 days
url: http://coursera.com
server response ok: True
domain expiration date: Domain name has been paid for more than 60 days
A Connection Error occured while sending request to:
http://roga.ikopyta
May be there is a mistake in url
url: http://roga.ikopyta
server response ok: False
domain expiration date: Whois has no information about expiration date
```

Also you can type:
```
$python check_sites_health.py -u http://wikipedia.org -d 60
```
You'll get:
```
url: http://wikipedia.org
server response ok: True
domain expiration date: Domain name has been paid for more than 60 days
```


### Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
