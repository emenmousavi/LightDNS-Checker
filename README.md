# LightDNS Checker

A Python script for checking a domain's DNS records and their DNS Zone provider.

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/lightdns-checker.git
    cd lightdns-checker
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the script:

    ```sh
    python lightdns-checker.py example.com
    ```

    This will output the DNS records for example.com.

## Options

* `-t <record type>`: Only show records of the specified type (e.g. `-t A`)
* `-n <record name>`: Only show records with the specified name (e.g. `-n www`)

## License

This project is licensed under the [MIT License](LICENSE).
