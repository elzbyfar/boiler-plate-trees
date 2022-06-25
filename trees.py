class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_array(self):
        '''Returns the tree's node values as an array'''
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
        '''Creates a Tree from an array of values.'''
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
    def __init__(self, root=None):
        self.root = root
        self.height = self._find_height_(root)

    def visualize(self: TreeNode) -> str:
        '''Returns a string formatted as a Binary Tree'''
        rows = self._split_nodes_by_row_()
        processed_rows = []

        for i, row in enumerate(rows):
            indent_width = self._indenter_(i)
            space_width = self._spacer_(i)

            indent = " " * indent_width
            joiner = " " * space_width
            spaced_row = joiner.join(row)
            processed_rows.append(indent + spaced_row)

        stringified_rows = "\n\n".join(processed_rows)
        return stringified_rows

    # Private Helpers
    def _split_nodes_by_row_(self: TreeNode):
        rows = []
        queue = [self.root]

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
            rows.append(row)
        return rows

    def _find_height_(self: TreeNode, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self._find_height_(root.left), self._find_height_(root.right))

    def _spacer_(self: TreeNode, index: int) -> int:
        '''Creates space_width between node values'''
        return 2 ** (self.height - index + 1) - 1

    def _indenter_(self: TreeNode, index: int) -> int:
        '''Creates indent_width to support tree-shaped output'''
        return 2 ** (self.height - index) - 2
