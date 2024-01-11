from days.day08 import Node, get_starting_list


class TestNode:
    def test_init(self):
        mock_left = 'eyy'
        mock_right = 'yo'
        mock_node_data = f' ({mock_left}, {mock_right})'
        mock_node = Node(mock_node_data)
        assert mock_node.left == mock_left
        assert mock_node.right == mock_right


class TestGetStartingList:
    mock_network = {
        'AAA': 'what',
        'BBB': 'huh',
        'CCA': 'yup',
        'ZZZ': 'sleep',
    }

    def test_all_start(self):
        actual = get_starting_list(self.mock_network)
        expected = ['AAA', 'CCA']
        assert actual == expected
