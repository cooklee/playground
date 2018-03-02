
def get_next_id():
    id_counter = 1
    while True:
        yield id_counter
        id_counter += 1


class Node(object):

    generator_node_id = get_next_id()
    LEFT_LEAF = 0
    RIGHT_LEAF = 1
    LEAF_DESCRIPTUON = ['left', 'right']

    def __init__(self, left_leaf=None, right_leaf=None):
        self.node_id = next(Node.generator_node_id)
        self.leafs = [left_leaf, right_leaf]

    def add_right_leaf(self, node):
        self.__add_leaf__(node, Node.RIGHT_LEAF)

    def add_left_leaf(self, node):
        self.__add_leaf__(node, Node.LEFT_LEAF)

    def get_left_leaf(self):
        return self.leafs[Node.LEFT_LEAF]

    def get_right_leaf(self):
        return self.leafs[Node.RIGHT_LEAF]

    def __add_leaf__(self, node, which_leaf):
        """
        this is function that shouldn't be use directly
        :param node:
        0 -> left leaf
        1 -> right leaf
        :param which_leaf:
        :return: None
        """

        if self.leafs[which_leaf] is not None:
            raise Exception('{} leaf is not None'.format(Node.LEAF_DESCRIPTUON[which_leaf]))

        self.leafs[which_leaf] = node


class BinaryTree(object):

    def __init__(self, root_node=None):
        if root_node is None:
            self.root = Node()
        else:
            self.root = root_node

    def add_left_leaf(self, node_id, node):
        node_to_add_leaf = self.search_for_node(node_id)
        node_to_add_leaf.add_left_leaf(node)

    def add_right_leaf(self, node_id, node):
        node_to_add_leaf = self.search_for_node(node_id)
        node_to_add_leaf.add_right_leaf(node)

    def search_for_node(self, id_node_to_find):
        return self.find_node(id_node_to_find, self.root)

    def find_node(self, id_node_to_find, current_node):
        if current_node is None:
            return current_node
        if current_node.node_id == id_node_to_find:
            return current_node

        left_node = self.find_node(id_node_to_find, current_node.get_left_leaf())

        if left_node is None:
            return self.find_node(id_node_to_find, current_node.get_right_leaf())
        return left_node

