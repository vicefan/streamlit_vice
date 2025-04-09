import requests
from bs4 import BeautifulSoup

start_url = "https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2/recent-events/"
sdog = "https://www.sherdog.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

result = []

for i in range(8, 0, -1):
    response = requests.get(start_url + str(i), headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.select_one("#recent_tab > table")

    a_tags = table.find_all('a', href=True)[::-1]
    events = [a['href'] for a in a_tags]

    for event in events:
        print(f"Processing event: {event.split('/')[-1]}")
        event_url = sdog + event
        response = requests.get(event_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.select_one("body > div.wrapper > div.inner-wrapper > div.col-left > section:nth-child(3) > div > table")
        matches = soup.find_all('meta', itemprop='name')
        for match in matches:
            result.append(match['content'].split(" vs "))

print(result)