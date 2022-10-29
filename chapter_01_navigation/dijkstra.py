from typing import Dict, NamedTuple, Tuple


class Node(NamedTuple):
    name: str
    direct_paths: Tuple["DirectPath"]


class DirectPath(NamedTuple):
    end_node: Node
    length: float


class Path(NamedTuple):
    nodes: Tuple[Node]
    length: float


class Network(NamedTuple):
    nodes: Tuple[Node]

    def get_best_path(self, start_node: Node, end_node: Node) -> Path:
        traversed_nodes = {start_node: Path(nodes=(start_node,), length=0.0)}

        while True:
            if end_node in traversed_nodes:
                return traversed_nodes[end_node]

            path_to_next_node = min(self.get_possible_paths(traversed_nodes), key=lambda path: path.length)
            traversed_nodes[path_to_next_node.nodes[-1]] = path_to_next_node

    def get_possible_paths(self, traversed_nodes: Dict[Node, Path]):
        for node, path in traversed_nodes.items():
            for direct_path in node.direct_paths:
                if direct_path.end_node not in traversed_nodes:
                    yield Path(nodes=(*path.nodes, direct_path.end_node), length=path.length + direct_path.length)
