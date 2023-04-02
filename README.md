# LightDNS Checker

LightDNS Checker is a Python script for checking a domain's DNS records and their DNS zone provider. The tool is useful for system administrators, network engineers, and security analysts who need to monitor DNS records and ensure they are correctly configured.

# Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/lightdns-checker.git
cd lightdns-checker```

2. Install the dependencies:
```pip install -r requirements.txt```


# Usage
Run the script with the domain name as an argument:
```python lightdns_checker.py example.com```
The script will display the DNS records for the domain and their DNS zone provider.

# Filtering
You can filter the DNS records by type or name. To filter by type, use the -t or --type option followed by the record type (e.g., A, MX, NS, TXT, etc.):
```python lightdns_checker.py example.com -t MX```

To filter by name, use the -n or --name option followed by the record name:
```python lightdns_checker.py example.com -n www```
You can also combine both options to filter by both type and name.

# Output Formats
The script supports two output formats: json and table. By default, the output is displayed in a human-readable table format. To output in JSON format, use the -f or --format option:
```python lightdns_checker.py example.com -f json```

# Help
To display the help message with all the available options, use the -h or --help option:
```python lightdns_checker.py -h```

# Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
