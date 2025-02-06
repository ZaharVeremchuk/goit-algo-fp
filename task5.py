import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def get_hex_color(count):
    # Генеруємо HEX колір на основі порядкового номера
    # Кольори змінюються від темних до світлих відтінків
    r = hex(min(255, count * 25))[2:].zfill(2)
    g = hex(min(255, count * 50))[2:].zfill(2)
    b = hex(min(255, count * 75))[2:].zfill(2)
    return f"#{r}{g}{b}"

def dfs(node, visited, count):
    if node:
        visited.add(node.id)
        node.color = get_hex_color(count[0])
        count[0] += 1
        dfs(node.left, visited, count)
        dfs(node.right, visited, count)

def bfs(node, count):
    if node:
        visited = set()
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current.id not in visited:
                visited.add(current.id)
                current.color = get_hex_color(count[0])
                count[0] += 1
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину
visited = set()
count = [1]
dfs(root, visited, count)
draw_tree(root)

# Повертаємо кольори до початкових та робимо обхід в ширину
def reset_colors(node):
    if node:
        node.color = "skyblue"
        reset_colors(node.left)
        reset_colors(node.right)

reset_colors(root)
count = [1]
bfs(root, count)
draw_tree(root)