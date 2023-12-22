from pyvis.network import Network
import webbrowser
import os


class GraphView:
    def __init__(self):
        self.bg_col = "#1e1e1e"
        self.accent_col = "#855de8"
        self.node_size = 10

        self.graph = Network(bgcolor=self.bg_col)

    def populate_graph_from_pairs(self, node_pairs):
        if not node_pairs:
            raise Exception(
                "No node pairs found. Please check if the provided Notion workspace url is correct and the integration has access to your workspace.")
        for parent, child in node_pairs:
            self.graph.add_node(parent, label=parent, color=self.accent_col, size=self.node_size)
            self.graph.add_node(child, label=child, color=self.accent_col, size=self.node_size)

            self.graph.add_edge(parent, child, smooth='False')

    def create_graph(self):
        options = """const options = {
              "edges": {
                "color": {
                  "inherit": true
                },
                "selfReferenceSize": null,
                "selfReference": {
                  "angle": 0.7853981633974483
                },
                "smooth": false
              },
              "interaction": {
                "hover": true
              },
              "physics": {
                "barnesHut": {
                  "springLength": 60,
                  "springConstant": 0.005
                },
                "minVelocity": 0.75
              }
            }"""
        self.graph.set_options(options=options)
        self.graph.height = '1000px'

        return self.graph

    def set_title(self, t, path):
        styled_content = f'<h1 style="text-align: center; color: white; background-color: {self.bg_col};">{t}</h1>'
        with open(path, "r+") as html_file:
            styled_content += html_file.read()
            html_file.seek(0)
            html_file.write(styled_content)

    def display_graph(self, title, node_pairs):
        folder_name = "graphs"
        os.makedirs(folder_name, exist_ok=True)

        html_path = os.path.join(folder_name, title + ".html")

        self.create_graph()
        self.populate_graph_from_pairs(node_pairs)
        self.graph.save_graph(html_path)
        self.set_title(title, html_path)

        webbrowser.open(html_path)
