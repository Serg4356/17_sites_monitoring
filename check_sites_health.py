import whois
import requests
import datetime
import types
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='''
        Program checks sites health: is server respond with less than 400
        and if domain payment expires in 30 days
        ''')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='Input site url')
    group.add_argument('-p',
                       '--path',
                       help='Input path to txt file with urls')
    parser.add_argument('-d',
                        '--days',
                        type=int,
                        default=30,
                        help='Days of domain expiration'
                        ' check (30 for default)')

    return parser


def load_urls4check(path):
    with open(path, 'r') as urls_file:
        return [url for url in urls_file.read().split('\n') if url]


def is_server_respond_ok(url):
    response = requests.get(url)
    return response.ok


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[-1]
    return expiration_date


def is_expired(expiration_date, days_before_expiration):
    if not expiration_date:
        return 'Whois has no information about expiration date'
    time_delta = expiration_date.replace(tzinfo=None) - datetime.datetime.now()
    if time_delta.days > days_before_expiration:
        return ('Domain name has been paid for'
                ' more than {} days'.format(days_before_expiration))
    else:
        return f'Domain name payment expires in {days_before_expiration} days'


if __name__ == '__main__':
    parser = create_parser()
    arguments = parser.parse_args()
    if arguments.url is None:
        urls4check = load_urls4check(arguments.path)
    else:
        urls4check = [arguments.url]
    for url in urls4check:
        domain = url.split('/')[-1]
        server_respond_ok = False
        try:
            server_respond_ok = is_server_respond_ok(url)
        except requests.exceptions.ConnectionError:
            print('A Connection Error occured while sending request to:')
            print(url)
            print('May be there is a mistake in url')
        domain_expiration_date = get_domain_expiration_date(domain)
        print(('url: {}\nserver response ok: {}\ndomain '
               'expiration date: {}'.format(url,
                                            server_respond_ok,
                                            is_expired(
                                                domain_expiration_date,
                                                arguments.days))))
