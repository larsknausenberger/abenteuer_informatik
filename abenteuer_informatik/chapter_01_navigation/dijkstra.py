from typing import Dict, NamedTuple, Tuple


class DirectPath(NamedTuple):
    """connection to an adjacent node"""

    end_node_id: str
    length: float


class Node(NamedTuple):
    """node in network with connections to adjacent nodes"""

    direct_paths: Tuple[DirectPath, ...]


class Path(NamedTuple):
    """a path from one node to another that may traverse other nodes

    node_ids[0] is the start node
    node_ids[-1] is the end node
    """

    node_ids: Tuple[str, ...]
    length: float


class Network:
    """a network of nodes

    "nodes" is a dictionary with the node_ids (of type str) as the keys and nodes (of type Node) as the values"""

    def __init__(self, nodes: Dict[str, Node]):
        # validate nodes
        for node_id, node in nodes.items():
            for direct_path in node.direct_paths:
                if direct_path.end_node_id not in nodes:
                    raise KeyError(
                        f'Network invalid: Node with ID "{node_id}" has a direct path to a non-existing node with ID "{direct_path.end_node_id}".'
                    )

        self.nodes = nodes

    def get_best_path(self, start_node_id: str, end_node_id: str) -> Path:
        """returns ideal path (with minimal length / cost) from start node to end node"""

        # validate start node exists
        try:
            self.nodes[start_node_id]
        except KeyError as exc:
            raise KeyError(f'Start node "{start_node_id}" does not exist.') from exc

        # validate end node exists
        try:
            self.nodes[end_node_id]
        except KeyError as exc:
            raise KeyError(f'End node "{end_node_id}" does not exist.') from exc

        # initialize traversed nodes with start node
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
        """returns possible paths to new, yet to be traversed, nodes

        paths to already traversed nodes are omitted"""

        for node_id, path in traversed_node_ids.items():
            node = self.nodes[node_id]

            for direct_path in node.direct_paths:
                if direct_path.end_node_id not in traversed_node_ids:
                    yield Path(
                        node_ids=(*path.node_ids, direct_path.end_node_id), length=path.length + direct_path.length
                    )
