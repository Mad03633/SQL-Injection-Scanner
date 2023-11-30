import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
ERROR_MESSAGES = {"quoted string not properly terminated", "unclosed quotation mark after the character string", "you have an error in your SQL syntax"}

def get_forms(url):
    # Function to get all forms
    soup = BeautifulSoup(requests.get(url, headers={"User-Agent": USER_AGENT}).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    # Function to extract form details
    details_of_form = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    details_of_form['action'] = action
    details_of_form['method'] = method
    details_of_form['inputs'] = inputs
    return details_of_form

def vulnerable(response):
    # Function to check if the response contains SQL injection error messages
    for error in ERROR_MESSAGES:
        if error in response.content.decode().lower():
            return True
    return False

def sql_injection_scan(url):
    # Main function to scann for SQL injection vulnerabilities
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")

    for form in forms:
        details = form_details(form)
        res = None
    
        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag['name']] = input_tag["value"] + i
                elif input_tag["type"] != "submit":
                    data[input_tag['name']] = f"test{i}"
                
            print(url)
            form_details(form)

            if details["method"] == "post":
                try:
                    res = requests.post(url, data=data, headers={"User-Agent": USER_AGENT})
                except requests.RequestException as e:
                    print(f"Error during POST request: {e}")
                    continue
            elif details["method"] == "get":
                try:
                    res = requests.get(url, params=data, headers={"User-Agent": USER_AGENT})
                except requests.RequestException as e:
                    print(f"Error during GET request: {e}")
                    continue
            
        if res and vulnerable(res):
            print("SQL injection attack vulnerability in link:", url)
        else:
            print("No SQL injection attack vulnerability detected")
            break

if __name__ == "__main__":
    url_to_be_checked = "https://lichess.org"
    sql_injection_scan(url_to_be_checked)
