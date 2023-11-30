# SQL Injection Scanner

This Python script is designed to identify potential SQL injection vulnerabilities in web applications by analyzing HTML forms and submitting payloads to the server.

## Features

- Analyzes HTML forms on a given webpage.
- Submits payloads to form inputs to detect SQL injection vulnerabilities.
- Checks for common SQL error messages in the HTTP response.

## Usage

```
python scan.py [URL]
```
Replace [URL] with the actual URL of the target web application you want to scan.

## Example
Output will be:
```
[+] Detected 1 forms on https://lichess.org.
https://lichess.org
https://lichess.org
No SQL injection attack vulnerability detected
```

## Configurations

- Set the USER_AGENT variable in the script to your desired User-Agent string.
- Customize the ERROR_MESSAGES set to match common SQL error messages in your application.

## Disclaimer

This script is provided for educational and informational purposes only. Use this tool responsibly and only on systems for which you have explicit permission to perform security testing. Unauthorized testing is illegal and unethical.
