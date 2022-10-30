import pytest
from abenteuer_informatik.chapter_01_navigation.dijkstra import Node, Network, DirectPath, Path


@pytest.fixture
def network():
    return Network(
        {
            "A": Node(
                direct_paths=(
                    DirectPath(end_node_id="M", length=6.7),
                    DirectPath(end_node_id="B", length=14.3),
                    DirectPath(end_node_id="N", length=3.8),
                    DirectPath(end_node_id="D", length=6.6),
                )
            ),
            "B": Node(
                direct_paths=(
                    DirectPath(end_node_id="A", length=14.3),
                    DirectPath(end_node_id="X", length=4.9),
                    DirectPath(end_node_id="I", length=7.0),
                    DirectPath(end_node_id="H", length=5.6),
                    DirectPath(end_node_id="Z", length=6.2),
                    DirectPath(end_node_id="D", length=13.0),
                )
            ),
            "C": Node(
                direct_paths=(
                    DirectPath(end_node_id="M", length=5.6),
                    DirectPath(end_node_id="I", length=8.2),
                    DirectPath(end_node_id="X", length=4.6),
                )
            ),
            "D": Node(
                direct_paths=(
                    DirectPath(end_node_id="A", length=6.6),
                    DirectPath(end_node_id="N", length=4.1),
                    DirectPath(end_node_id="B", length=13.0),
                    DirectPath(end_node_id="L", length=18.9),
                )
            ),
            "E": Node(
                direct_paths=(
                    DirectPath(end_node_id="G", length=12.1),
                    DirectPath(end_node_id="K", length=6.2),
                    DirectPath(end_node_id="F", length=15.6),
                    DirectPath(end_node_id="O", length=19.5),
                )
            ),
            "F": Node(
                direct_paths=(
                    DirectPath(end_node_id="P", length=11.6),
                    DirectPath(end_node_id="O", length=2.9),
                    DirectPath(end_node_id="E", length=15.6),
                    DirectPath(end_node_id="K", length=6.1),
                )
            ),
            "G": Node(
                direct_paths=(
                    DirectPath(end_node_id="L", length=11.8),
                    DirectPath(end_node_id="Y", length=5.5),
                    DirectPath(end_node_id="K", length=11.5),
                    DirectPath(end_node_id="E", length=12.1),
                )
            ),
            "H": Node(
                direct_paths=(
                    DirectPath(end_node_id="B", length=5.6),
                    DirectPath(end_node_id="I", length=13.4),
                    DirectPath(end_node_id="P", length=7.1),
                    DirectPath(end_node_id="K", length=6.0),
                    DirectPath(end_node_id="Y", length=5.9),
                    DirectPath(end_node_id="L", length=21.1),
                )
            ),
            "I": Node(
                direct_paths=(
                    DirectPath(end_node_id="M", length=9.0),
                    DirectPath(end_node_id="P", length=10.5),
                    DirectPath(end_node_id="H", length=13.4),
                    DirectPath(end_node_id="B", length=7.0),
                    DirectPath(end_node_id="C", length=8.2),
                )
            ),
            "K": Node(
                direct_paths=(
                    DirectPath(end_node_id="H", length=6.0),
                    DirectPath(end_node_id="P", length=5.1),
                    DirectPath(end_node_id="F", length=6.1),
                    DirectPath(end_node_id="E", length=6.2),
                    DirectPath(end_node_id="G", length=11.5),
                    DirectPath(end_node_id="Y", length=3.6),
                )
            ),
            "L": Node(
                direct_paths=(
                    DirectPath(end_node_id="D", length=18.9),
                    DirectPath(end_node_id="Z", length=7.8),
                    DirectPath(end_node_id="H", length=21.1),
                    DirectPath(end_node_id="G", length=11.8),
                )
            ),
            "M": Node(
                direct_paths=(
                    DirectPath(end_node_id="I", length=9.0),
                    DirectPath(end_node_id="C", length=5.6),
                    DirectPath(end_node_id="X", length=2.3),
                    DirectPath(end_node_id="A", length=6.7),
                )
            ),
            "N": Node(
                direct_paths=(
                    DirectPath(end_node_id="A", length=3.8),
                    DirectPath(end_node_id="X", length=6.4),
                    DirectPath(end_node_id="Z", length=5.8),
                    DirectPath(end_node_id="D", length=4.1),
                )
            ),
            "O": Node(
                direct_paths=(
                    DirectPath(end_node_id="P", length=18.2),
                    DirectPath(end_node_id="Q", length=5.3),
                    DirectPath(end_node_id="E", length=19.5),
                    DirectPath(end_node_id="F", length=2.9),
                )
            ),
            "P": Node(
                direct_paths=(
                    DirectPath(end_node_id="I", length=10.5),
                    DirectPath(end_node_id="O", length=18.2),
                    DirectPath(end_node_id="F", length=11.6),
                    DirectPath(end_node_id="K", length=5.1),
                    DirectPath(end_node_id="H", length=7.1),
                )
            ),
            "Q": Node(direct_paths=(DirectPath(end_node_id="O", length=5.3),)),
            "X": Node(
                direct_paths=(
                    DirectPath(end_node_id="M", length=2.3),
                    DirectPath(end_node_id="C", length=4.6),
                    DirectPath(end_node_id="B", length=4.9),
                    DirectPath(end_node_id="N", length=6.4),
                )
            ),
            "Y": Node(
                direct_paths=(
                    DirectPath(end_node_id="Z", length=4.5),
                    DirectPath(end_node_id="H", length=5.9),
                    DirectPath(end_node_id="K", length=3.6),
                    DirectPath(end_node_id="G", length=5.5),
                )
            ),
            "Z": Node(
                direct_paths=(
                    DirectPath(end_node_id="N", length=5.8),
                    DirectPath(end_node_id="B", length=6.2),
                    DirectPath(end_node_id="Y", length=4.5),
                    DirectPath(end_node_id="L", length=7.8),
                )
            ),
        }
    )


@pytest.mark.parametrize(
    argnames=("start_node_id", "end_node_id", "expected"),
    argvalues=[
        ("I", "O", Path(node_ids=("I", "P", "K", "F", "O"), length=24.6)),  # Imstadt to Oppenheim
        ("I", "I", Path(node_ids=("I",), length=0.0)),  # Imstadt to Imstadt
        ("L", "E", Path(node_ids=("L", "Z", "Y", "K", "E"), length=22.1)),  # Lupera to Eindhofen
    ],
)
def test_best_path(network: Network, start_node_id: str, end_node_id: str, expected: Path):
    best_path = network.get_best_path(start_node_id=start_node_id, end_node_id=end_node_id)
    assert best_path.node_ids == expected.node_ids
    assert best_path.length == pytest.approx(expected.length)


def test_no_possible_path():
    network = Network(
        nodes={
            "A": Node(direct_paths=(DirectPath(end_node_id="B", length=6.7),)),
            "B": Node(direct_paths=()),
        }
    )
    with pytest.raises(ValueError) as excinfo:
        network.get_best_path(start_node_id="B", end_node_id="A")
    assert "no path" in str(excinfo.value).lower()


def test_invalid_start_node_id(network):
    with pytest.raises(KeyError) as excinfo:
        network.get_best_path(start_node_id="R", end_node_id="E")
    assert 'start node "r" does not exist' in str(excinfo.value).lower()


def test_invalid_end_node_id(network):
    with pytest.raises(KeyError) as excinfo:
        network.get_best_path(start_node_id="E", end_node_id="R")
    assert 'end node "r" does not exist' in str(excinfo.value).lower()


def test_invalid_network():
    with pytest.raises(KeyError) as excinfo:
        Network(
            nodes={
                "A": Node(direct_paths=(DirectPath(end_node_id="X", length=6.7),)),
            }
        )
    assert "network invalid" in str(excinfo.value).lower()
