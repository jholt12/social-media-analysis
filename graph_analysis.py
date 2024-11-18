import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    """Create a directed graph with users and posts."""
    graph = nx.DiGraph()

    # Example data
    graph.add_node("user123", type="user", name="John Doe")
    graph.add_node("post001", type="post", views=20, comments=5)
    graph.add_edge("user123", "post001", relation="author")

    return graph

def calculate_post_importance(graph):
    """Calculate and assign importance scores to post nodes in the graph."""
    for node in graph.nodes:
        if graph.nodes[node].get('type') == 'post':
            views = graph.nodes[node].get('views', 0)
            comments = graph.nodes[node].get('comments', 0)
            importance = views + 2 * comments
            graph.nodes[node]['importance'] = importance

def visualize_graph(graph):
    """Visualize the graph, highlighting posts by importance."""
    node_colors = [
        'blue' if graph.nodes[node]['type'] == 'user' else 'red'
        for node in graph
    ]
    sizes = [
        300 if graph.nodes[node]['type'] == 'user' else 500 + graph.nodes[node].get('importance', 0)
        for node in graph
    ]
    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=sizes)
    plt.show()

if __name__ == "__main__":
    graph = create_graph()
    calculate_post_importance(graph)
    visualize_graph(graph)