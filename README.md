# LightDNS Checker

A Python script for checking a domain's DNS records and their DNS Zone provider.

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/emenmousavi/lightdns-checker.git
    cd lightdns-checker
    ```

2. Install the required packages:

    ```sh
    pip install dnspython
    ```

3. Run the script:

    ```sh
    python lightdns-checker.py example.com
    ```

Note: Replace "example.com" with the domain that you want to check. You can also use the -t and -n options to retrieve specific DNS records by type and name. For example:
    ```sh
    python lightdns-checker.py example.com -t MX
    ```
    ```sh
    python lightdns-checker.py example.com -n www
    ```

4. The program will print out the DNS records for the specified domain, as well as the DNS Zone provider.

![alt text]([relative/path/to/img.jpg](https://github.com/emenmousavi/LightDNS-Checker/blob/main/Atest.png))

## Options

* `-t <record type>`: Only show records of the specified type (e.g. `-t A`)
* `-n <record name>`: Only show records with the specified name (e.g. `-n www`)

## License

This project is licensed under the [MIT License](https://github.com/emenmousavi/LightDNS-Checker/blob/main/LICENSE).
