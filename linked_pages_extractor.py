from urllib.parse import urljoin
import json


class LinkedPagesExtractor:
    def __init__(self, notion):
        self.notion = notion

    def extract_linked_pages(self, page_id, page_links):
        url = urljoin(self.notion.NOTION_BASE_URL, f"blocks/{page_id}/children")

        response = self.notion.session.get(url)
        data = response.json()

        try:
            for block in data["results"]:
                if block.get("type") == "child_page":
                    child_id = block["id"]
                    link = [page_id, child_id]
                    page_links.append(link)

                    self.extract_linked_pages(child_id, page_links)

        except KeyError:
            print("Invalid Notion workspace ID or empty page. Unable to extract pages.")
