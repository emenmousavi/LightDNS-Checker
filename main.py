import dns.resolver
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Check a domain\'s DNS records and DNS Zone provider.')
parser.add_argument('domain', help='Domain name to check')
parser.add_argument('-t', '--type', help='DNS record type to retrieve (e.g. A, MX, TXT)')
parser.add_argument('-n', '--name', help='DNS record name to retrieve (e.g. www)')
args = parser.parse_args()

# Retrieve DNS records
answers = dns.resolver.query(args.domain, args.type)

# Print DNS records
if args.name:
    for rdata in answers:
        if args.name == rdata.to_text().split()[0]:
            print(rdata)
else:
    for rdata in answers:
        print(rdata)

# Print DNS Zone provider
ns_answers = dns.resolver.query(args.domain, 'NS')
print('\nDNS Zone provider:', ns_answers[0])
