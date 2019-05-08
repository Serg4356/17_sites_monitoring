import whois
import requests
import datetime
import types
import argparse



def create_parser():
    parser = argparse.ArgumentParser(
        description='''
        Program checks sites health: is server respond with 200
        and if domain payment expires in 30 days
        ''')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='Input site url')
    group.add_argument('-p', '--path', help='Input path to txt file with urls')

    return parser


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
	parser = create_parser()
	arguments = parser.parse_args()
	if arguments.url is None:
		urls4check = load_urls4check(arguments.path)
	else:
		urls4check = [arguments.url]
	for url in urls4check:
		domain = url.split('/')[-1]
		print('url: {}\nserver response ok: {}\ndomain '
			'expiration date: {}'.format(url,
                                         is_server_respond_with_200(url),
                                         get_domain_expiration_date(domain)))

