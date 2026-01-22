

class Node:
    def __init__(self, pid):
        self.pid = pid
        self.left = None
        self.right = None

def insert(root, pid):
    if root is None:
        return Node(pid)
    if pid < root.pid:
        root.left = insert(root.left, pid)
    else:
        root.right = insert(root.right, pid)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.pid, end=" ")
        inorder(root.right)


root = None
product_ids = [105, 101, 110, 103, 108]

for pid in product_ids:
    root = insert(root, pid)

print("Sorted Product IDs:")
inorder(root)
