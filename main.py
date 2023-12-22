from notion_client import NotionClient
from linked_pages_extractor import LinkedPagesExtractor
from graph_view import GraphView


def main():
    while True:
        try:
            access_token = input("Enter your Notion API integration token: ")
            url = input("Enter the Notion workspace URL (found under Share > Copy Link): ")
            url = url.strip()

            print("Validating token and url...")
            notion = NotionClient(access_token)
            root_page_id, root_page_title = notion.extract_from_url(url)

            print("Extracting pages...")
            page_links = []
            LinkedPagesExtractor(notion).extract_linked_pages(root_page_id, page_links)
            titles_list = [[notion.get_page_title(link[0]), notion.get_page_title(link[1])] for link in page_links]
            print(f"Found {len(page_links)} links")

            print("Generating graph...")
            graph = GraphView()
            print("Graph created! Opening now...")
            graph.display_graph(root_page_title, titles_list)

            break
        except ValueError as e:
            print(e, "\n")
            retry = input("Do you want to retry? (y/n): ").lower()
            if retry != 'y':
                print("Exiting.")
                break


if __name__ == "__main__":
    main()
