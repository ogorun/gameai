from game import Game
from collections import Counter
import networkx as nx, os
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt



class MCSTTreeNode:
    sequence = 0

    def __init__(self, game: Game):
        self.id = self.__class__.sequence
        self.game = game
        self.n = 0
        self.s = 0
        self.children = []
        self.parent = None
        self.__class__.sequence += 1

    def append(self, node):
        self.children.append(node)
        node.parent = self

    def is_leaf(self):
        return len(self.children) == 0

    def depth(self):
        result = 0
        node = self
        while node.parent is not None:
            result += 1
            node = node.parent
        return result

    def to_str(self):
        return f"{self.id}: {self.s}/{self.n}"

    def draw(self, title, from_root=True):
        if from_root and self.parent is not None:
            root = self.parent
            while root.parent is not None:
                root = root.parent
        else:
            root = self

        dir = os.path.dirname(os.path.dirname(__file__)) + '/debug_images'
        G = nx.DiGraph()
        self._add_nod_to_graph(G, root, None)
        write_dot(G, f'{dir}/{title}.dot')

        # same layout using matplotlib with no labels
        fig, axis = plt.subplots(1, 1, figsize=(9,6))
        axis.set_title(title)
        pos=graphviz_layout(G, prog='dot')
        nx.draw(G, pos, ax=axis, with_labels=True, arrows=True)
        fig.savefig(f'{dir}/{title}.png')
        plt.close(fig)

    def _add_nod_to_graph(self, G, node, parent):
        G.add_node(node.to_str())
        if parent is not None:
            G.add_edge(parent.to_str(), node.to_str())
        for child in node.children:
            self._add_nod_to_graph(G, child, node)

    def leafs_counter(self, counter: Counter = None):
        if counter is None:
            counter = Counter()

        if self.is_leaf():
            counter[f"{self.depth()}_{self.n > 0}"] += 1

        for child in self.children:
            child.leafs_counter(counter)

        return counter
