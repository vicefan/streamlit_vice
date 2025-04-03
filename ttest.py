import requests

# Login URL and credentials
LOGIN_URL = 'https://www.credit.co.kr/ib20/mnu/BZWSGMMLO10'
USERNAME = 'dddooong2000'
PASSWORD = 'Chan0thug!'

# Create a session to persist the login
session = requests.Session()

# Login data
login_data = {
    'userId': USERNAME,
    'pwd': PASSWORD
}

# Send a POST request to login
response = session.post(LOGIN_URL, data=login_data)

# Check if login was successful
if response.status_code == 200:
    print('Login successful')
else:
    print('Login failed')

# URL to crawl after login
CRAWLING_URL = 'https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20?param=7J207LCsLDEs7LCsLOydtCxZ&uaCheck=Y'
response = session.get(CRAWLING_URL)

# Print the HTML content of the page
print(response.text)