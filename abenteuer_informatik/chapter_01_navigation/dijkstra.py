from typing import Dict, NamedTuple, Tuple


class DirectPath(NamedTuple):
    end_node_id: str
    length: float


class Node(NamedTuple):
    direct_paths: Tuple[DirectPath, ...]


class Path(NamedTuple):
    node_ids: Tuple[str, ...]
    length: float


class Network:
    def __init__(self, nodes: Dict[str, Node]):
        self.nodes = nodes

    def get_best_path(self, start_node_id: str, end_node_id: str) -> Path:
        traversed_nodes = {start_node_id: Path(node_ids=(start_node_id,), length=0.0)}

        while True:
            if end_node_id in traversed_nodes:
                return traversed_nodes[end_node_id]

            try:
                path_to_next_node = min(self.get_possible_paths(traversed_nodes), key=lambda path: path.length)
            except ValueError as exc:
                raise ValueError("No path found.") from exc
            traversed_nodes[path_to_next_node.node_ids[-1]] = path_to_next_node

    def get_possible_paths(self, traversed_node_ids: Dict[str, Path]):
        for node_id, path in traversed_node_ids.items():
            node = self.nodes[node_id]

            for direct_path in node.direct_paths:
                if direct_path.end_node_id not in traversed_node_ids:
                    yield Path(
                        node_ids=(*path.node_ids, direct_path.end_node_id), length=path.length + direct_path.length
                    )
