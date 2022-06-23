import math


class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_array(self):
        if not self:
            return []
        output = []
        q = [self]
        while q:
            node = q.pop(0)
            output.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return output

    def from_array(arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        stack = []

        if len(arr) > 1:
            stack.append([1, root, "left"])
        if len(arr) > 2:
            stack.append([2, root, "right"])

        while stack:
            [index, parent, direction] = stack.pop()
            if direction == "left":
                parent.left = TreeNode(arr[index])
            if direction == "right":
                parent.right = TreeNode(arr[index])

            left_child = index * 2 + 1
            right_child = (index + 1) * 2

            next_parent = parent.left if direction == "left" else parent.right

            if left_child < len(arr):
                stack.append([left_child, next_parent, "left"])

            if right_child < len(arr):
                stack.append([right_child, next_parent, "right"])

        return root


class TreePrinter():
    def __init__(self, root=None, base_width=3):
        self.root = root
        self.base_width = base_width

    def visualize(self: TreeNode) -> str:
        '''Returns a string formatted as a Binary Tree'''
        queue = [self.root]
        levels = []

        # visit and process every node in the queue
        # add each node's value to the row array
        while queue:
            queue_size = len(queue)
            row = []
            for _ in range(0, queue_size):
                node = queue.pop(0)
                value = node.value if isinstance(node.value, int) else "-"
                row.append(str(value))

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(row)

        output_rows = []
        tree_height = len(levels)
        for i, row in enumerate(levels):
            indent_width = 0
            space_width = self._spacer(i, tree_height)
            if i < tree_height - 1:
                indent_width = self._indenter_(
                    i, space_width, levels)
            if i < tree_height - 2:
                space_width = indent_width * 3 - 3

            indent = " " * indent_width
            joiner = " " * space_width
            spaced_row = joiner.join(row)
            output_rows.append("\t" + indent + spaced_row)
        return "\n\n".join(output_rows)

    # Private Helpers
    def __make_odd__(self: TreeNode, n: int) -> int:
        '''
        Adds 1 to the space between node values
        when the space between those values is even.
        Number of spaces should be odd to allow for symmetry.
        '''

        return n + 1 if n % 2 == 0 else n

    def _spacer(self: TreeNode, index: int, tree_height: int) -> int:
        '''Creates space_width between node values'''
        row_index = tree_height - index - 1
        space_width = self.base_width * 2 ** row_index
        return self.__make_odd__(space_width)

    def _indenter_(self, index, space_width, node_rows):
        '''Creates indent_width to support tree-shaped output'''
        tree_height = len(node_rows)
        indent_spaces = math.ceil((space_width - 1) / 2)
        if index == 0:
            # edge case handles root row
            # for best results, add a space for each node in the tree
            count = sum(len(row) for row in node_rows)

            # indentation for root row should be even number of spaces
            indent_spaces = count - 0 if count % 2 == 0 else count - 1
        elif index == tree_height - 2:
            # edge case handles second to last row
            indent_spaces -= 1
        return indent_spaces


# INSTRUCTIONS

# Color codes
red = '\33[31m'
green = '\33[32m'
yellow = '\33[33m'
blue = '\33[94m'
white = '\33[0m'

# EXAMPLES - JUST RUN THIS PYTHON FILE

# Create a single TreeNode
node = TreeNode(10)
print("\n")
print(f"{white}1. Create a single TreeNode\n")
print(f"   {white}node = TreeNode(10)")
print(f"   {white}print(node)\t\t ->   {green}{node}")
print(f"   {white}print(node.value)\t ->   {green}{node.value}")  # 10
print(f"   {white}print(node.left)\t ->   {red}{node.left}")  # None
print(f"   {white}print(node.right)\t ->   {red}{node.right}")  # None

# Create a Tree from an array
arr = [1, 2, 3, 4, 5, 6, 7, None, 9, None, 1, 2, None, 4, 5]
tree = TreeNode.from_array(arr)
print("\n")
print(f"{white}2. Create a Binary Tree from an array and print it as an array\n")
print(f"   {white}arr = [1,2,3,4,5,6,7,None,9,None,1,2,None,4,5]")
print(f"   {white}tree = TreeNode.from_array(arr)")
print(f"   {white}print(tree)\t\t ->   {green}{tree}")
print(f"   {white}print(tree.to_array())->   {green}{tree.to_array()}")

# Create a PrintableTree from Tree instance
printable_tree = TreePrinter(tree)
print("\n")
print(f"{white}3. Create a PrintableTree from a Tree instance\n")
print(f"   {white}printable_tree = TreePrinter(tree)")
print(f"   {white}print(printable_tree.visualize())\n")
print(f"{yellow}{printable_tree.visualize()}")

print("\n", white)

# Create a single TreeNode
# node = TreeNode(10)

# # Create a Tree from an array
# arr = [1, 2, 3, 4, 5, 6, 7, None, 9, None, 1, 2, None, 4, 5]
# tree = TreeNode.from_array(arr)

# # Create a PrintableTree from Tree instance
# printable_tree = TreePrinter(tree)
# print(printable_tree.visualize())
