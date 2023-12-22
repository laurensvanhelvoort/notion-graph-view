Notion Graph View
==============
**Notion Graph View** is a Python program that generates an Obsidian-style graph, visualizing linked pages within your Notion workspace. It extracts the connections between pages and displays them in an interactive graph in your web browser.
Features

- Automatically extract linked pages within your workspace to establish connections for graph visualization.
- Generate an interactive graph view, inspired by Obsidian, to visualize relationships between pages in your Notion workspace.
- This graph is saved as an `.html` file and automatically opened by the program upon creation.
## Example
Example graph:
> This example can be found in the examples folder of this project ('My Notion dashboard.html'). Open it in your browser to interact with it.

![image](https://github.com/laurensvanhelvoort/notion-graph-view/assets/74211074/1e37798c-d1c4-4c1d-9049-4aa436d73c36)

Zoomed and dragged:
![image](https://github.com/laurensvanhelvoort/notion-graph-view/assets/74211074/38dfaadb-a1c2-42d2-827b-be0daac615b2)


## Getting Started
Prerequisites

- Python 3.6 or higher
- Notion API Integration Token (obtained from Notion Integrations)
- Notion Workspace URL (found under Share > Copy Link)

## Installation
Clone the repository:

bash

    git clone https://github.com/laurensvanhelvoort/notion-graph-view.git
    cd notion-graph-view

### Install dependencies:

bash

    pip install -r requirements.txt

## Configuration

Configure the Notion API Integration:
1. Go to the Notion Integrations page.
2. Create a new integration and obtain the integration token.

Add the integration to the Notion workspace:
1. Go to the Notion page you want to create a graph of.
2. Open the page options and go to "Connections."
3. Add the integration to establish a connection with the workspace.

Usage
Run the script:

bash

    python main.py
Input your Notion API secret token and workspace ID you want to create the graph.
The generated HTML file will be opened in your default web browser and will be saved in the created folder 'graphs' in the directory of the project.
