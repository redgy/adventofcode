from days.day08 import Node, Network
import pytest


class TestNode:
    def test_init(self):
        mock_name = 'say'
        mock_left = 'eyy'
        mock_right = 'yo'
        mock_node = Node(mock_name, mock_left, mock_right)
        assert mock_node.name == mock_name
        assert mock_node.left == mock_left
        assert mock_node.right == mock_right


def get_mock_map(mock_map={'AAA': Node('AAA', 'left', 'right')}):
    return mock_map


@pytest.fixture
def mock_node():
    return Node('AAA', 'left', 'right')


@pytest.fixture
def mock_network():
    mock_map = get_mock_map()
    return Network(mock_map)


class TestNetwork:
    class TestInit:
        def test_empty(self):
            mock_map = {}
            mock_network = Network(mock_map)
            expected = mock_map
            actual = mock_network.map
            actual == expected

        def test_dict(self, mock_node, mock_network):
            expected = mock_node
            actual = mock_network.map['AAA']
            assert actual.left == expected.left
            assert actual.right == expected.right

    class TestAddNode:
        def test_new_node(self, mock_network):
            mock_node = Node('eyy', 'bee', 'see')
            mock_network.add(mock_node)
            expected = get_mock_map()
            expected[mock_node.name] = mock_node
            actual = mock_network.map
            assert actual == expected

        def test_existing_node(self, mock_node, mock_network):
            another_mock_node = Node(mock_node.name, 'anotherword', 'andanother')
            mock_network.add(mock_node)
            expected = get_mock_map()
            expected[mock_node.name] = Node(mock_node.name, another_mock_node.left, another_mock_node.right)
            actual = mock_network.map
            assert actual == expected
