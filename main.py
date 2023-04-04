import dns.resolver
import argparse

def retrieve_dns_records(domain, record_type=None, record_name=None):
    try:
        answers = dns.resolver.query(domain, record_type)
        if record_name:
            return [rdata for rdata in answers if record_name == rdata.to_text().split()[0]]
        else:
            return list(answers)
    except dns.resolver.NXDOMAIN:
        print('Error: Domain name is invalid')
        return []
    except dns.resolver.NoAnswer:
        print('Error: No answer found for the specified record type and name')
        return []
    except dns.exception.Timeout:
        print('Error: Connection timed out')
        return []

# Parse command line arguments
parser = argparse.ArgumentParser(description='Check a domain\'s DNS records and DNS Zone provider.')
parser.add_argument('domain', help='Domain name to check')
parser.add_argument('-t', '--type', help='DNS record type to retrieve (e.g. A, MX, TXT)')
parser.add_argument('-n', '--name', help='DNS record name to retrieve (e.g. www)')
args = parser.parse_args()

# Added my name :D
print('\033[1m' + 'LightDNS Checker by Emen Mousavi\n' + '\033[0m')

# Retrieve DNS records
dns_records = retrieve_dns_records(args.domain, args.type, args.name)

# Print DNS records
if dns_records:
    for rdata in dns_records:
        print(rdata)

# Print DNS Zone provider
dns_zone_providers = retrieve_dns_records(args.domain, 'NS')
if dns_zone_providers:
    print('\nDNS Zone provider:', dns_zone_providers[0])
