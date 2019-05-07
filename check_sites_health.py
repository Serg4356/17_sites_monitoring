import whois
import requests
import datetime
import types



def load_urls4check(path):
    with open(path, 'r') as urls_file:
        return [url for url in urls_file.read().split('\n') if url]


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.ok


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[-1]
    elif isinstance(expiration_date, type(None)):
        return 'Whois has no information about expiration date'
    time_delta = expiration_date.replace(tzinfo=None) - datetime.datetime.now()
    if time_delta.days > 30:
        return 'Domain name has been paid for more than 30 days'
    else:
        return 'Domain name payment expires in 30 days'


if __name__ == '__main__':
    urls4check = load_urls4check('urls.txt')
    for url in urls4check:
        domain = url.split('/')[-1]
        print('url: {}\nserver response ok: {}\ndomain '
              'expiration date: {}'.format(url,
                                           is_server_respond_with_200(url),
                                           get_domain_expiration_date(domain)))

