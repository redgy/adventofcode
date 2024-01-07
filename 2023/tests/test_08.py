from days.day08 import Node


class TestNode:
    def test_init(self):
        mock_left = 'eyy'
        mock_right = 'yo'
        mock_node = Node(mock_left, mock_right)
        assert mock_node.left == mock_left
        assert mock_node.right == mock_right


class TestNetwork:
    def test_init(self):
        pass
