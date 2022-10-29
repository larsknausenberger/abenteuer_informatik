from typing import NamedTuple, Tuple


class Node(NamedTuple):
    name: str


class DirectPath(NamedTuple):
    start_node: Node
    end_node: Node
    length: float


class Path(NamedTuple):
    nodes: Tuple[Node]

    @property
    def length(self):
        raise NotImplementedError


class Network(NamedTuple):
    direct_paths: Tuple[DirectPath]

    def get_best_path(self, start_node: Node, end_node: Node):
        raise NotImplementedError
