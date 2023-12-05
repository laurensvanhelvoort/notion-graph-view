import requests
from urllib.parse import urljoin
import re


class NotionClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            'Authorization': f"Bearer {self.access_token}",
            'Notion-Version': '2022-06-28'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.NOTION_BASE_URL = 'https://api.notion.com/v1/'

    def get_page_title(self, page_id):
        url = urljoin(self.NOTION_BASE_URL, f"pages/{page_id}")
        response = self.session.get(url)
        data = response.json()

        title = data.get('properties', {}).get('title', {}).get('title', [{'plain_text': 'Title not found'}])[0].get(
            'plain_text')
        return title

    def extract_from_url(self, url):
        match = re.search(r"(?<=-)([a-zA-Z\d]+)(?=\?)", url)
        if match:
            root_page_id = match.group(0)

            title_match = re.search(r"(?<=notion.so/)[^?]+", url)
            if title_match:
                sanitized_page_title = title_match.group(0).replace(f"-{root_page_id}", "").replace("-", " ")

                return root_page_id, sanitized_page_title
            else:
                raise Exception("Invalid URL format. Unable to extract root page title.")
        else:
            raise Exception("Invalid URL format. Unable to extract root page ID.")
