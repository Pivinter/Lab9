import unittest
from Lab9 import Node, insert, build_binary_search_tree, count_leaf_nodes


class TestNode(unittest.TestCase):

    def test_node_init(self):
        node = Node(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_insert(self):
        root = None
        root = insert(root, 5)
        root = insert(root, 3)
        root = insert(root, 7)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.left.value, 3)
        self.assertEqual(root.right.value, 7)

    def test_build_binary_search_tree(self):
        elements = [5, 3, 7, 1, 4, 6, 8]
        root = build_binary_search_tree(elements)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.left.value, 3)
        self.assertEqual(root.right.value, 7)
        self.assertEqual(root.left.left.value, 1)
        self.assertEqual(root.left.right.value, 4)
        self.assertEqual(root.right.left.value, 6)
        self.assertEqual(root.right.right.value, 8)

    def test_count_leaf_nodes(self):
        elements = [5, 3, 7, 1, 4, 6, 8]
        root = build_binary_search_tree(elements)
        count = count_leaf_nodes(root)
        self.assertEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
