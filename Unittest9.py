import unittest
import random
from Lab9 import build_tree, count_leaf_nodes, dict_to_tree, find_nodes_with_one_child, find_nodes_with_two_children, find_nodes_without_children, insert_node, load_tree_from_file, remove_node_with_no_children, remove_node_with_one_child, remove_node_with_two_children, save_tree_to_file, tree_to_dict


class TestTreeNodeFunctions(unittest.TestCase):

    def setUp(self):
        self.root = build_tree(10)

    def test_insert_node(self):
        tree = None
        values = [random.randint(1, 100) for _ in range(5)]

        for value in values:
            tree = insert_node(tree, value)

        for value in values:
            self.assertIsNotNone(self.find_node(tree, value))

    def find_node(self, root, value):
        if root is None:
            return None

        if root.value == value:
            return root

        if value < root.value:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)

    def test_count_leaf_nodes(self):
        leaf_nodes_count = count_leaf_nodes(self.root)
        self.assertGreaterEqual(leaf_nodes_count, 1)

    def test_remove_node_with_no_children(self):
        nodes_without_children = find_nodes_without_children(self.root)

        if nodes_without_children:
            value_to_remove = nodes_without_children[0]
            self.root = remove_node_with_no_children(self.root, value_to_remove)
            self.assertIsNone(self.find_node(self.root, value_to_remove))

    def test_find_nodes_without_children(self):
        nodes_without_children = find_nodes_without_children(self.root)
        for node_value in nodes_without_children:
            node = self.find_node(self.root, node_value)
            self.assertIsNone(node.left)
            self.assertIsNone(node.right)

    def test_remove_node_with_one_child(self):
        nodes_with_one_child = find_nodes_with_one_child(self.root)

        if nodes_with_one_child:
            value_to_remove = nodes_with_one_child[0]
            self.root = remove_node_with_one_child(self.root, value_to_remove)
            self.assertIsNone(self.find_node(self.root, value_to_remove))

    def test_remove_node_with_two_children(self):
        nodes_with_two_children = find_nodes_with_two_children(self.root)

        if nodes_with_two_children:
            value_to_remove = nodes_with_two_children[0]
            self.root = remove_node_with_two_children(self.root, value_to_remove)
            self.assertIsNone(self.find_node(self.root, value_to_remove))

    def test_find_nodes_with_two_children(self):
        nodes_with_two_children = find_nodes_with_two_children(self.root)
        for node_value in nodes_with_two_children:
            node = self.find_node(self.root, node_value)
            self.assertIsNotNone(node.left)
            self.assertIsNotNone(node.right)

    def test_tree_to_dict(self):
        tree_dict = tree_to_dict(self.root)
        self.assertIsNotNone(tree_dict)
        self.assertEqual(tree_dict["value"], self.root.value)

    def test_dict_to_tree(self):
        tree_dict = tree_to_dict(self.root)
        new_root = dict_to_tree(tree_dict)
        self.assertIsNotNone(new_root)
        self.assertEqual(new_root.value, self.root.value)

if __name__ == '__main__':
    unittest.main()
