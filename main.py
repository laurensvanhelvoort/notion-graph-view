from notion_client import NotionClient
from linked_pages_extractor import LinkedPagesExtractor
from graph_view import GraphView


def main():
    access_token = "..."
    url = "..."

    notion = NotionClient(access_token)
    root_page_id, root_page_title = notion.extract_from_url(url)

    page_links = []
    LinkedPagesExtractor(notion).extract_linked_pages(root_page_id, page_links)
    titles_list = [[notion.get_page_title(link[0]), notion.get_page_title(link[1])] for link in page_links]

    graph = GraphView()
    graph.display_graph(root_page_title, titles_list)


if __name__ == "__main__":
    main()
