class Node:
    def __init__(self, title):
        self.data = title
        self.left = None
        self.right = None
def insert(root, title):
    if root is None:
        return Node(title)

    if title.lower() < root.data.lower():
        root.left = insert(root.left, title)
    else:
        root.right = insert(root.right, title)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)
def preorder(root):
    if root is not None:
        print(root.data, end=" -> ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" -> ")
root = None
n = int(input("Enter number of books: "))
print("Enter the book titles:")
for i in range(n):
    title = input()
    root = insert(root, title)
print("\nInorder Traversal:")
inorder(root)
print("\n\nPreorder Traversal:")
preorder(root)
print("\n\nPostorder Traversal:")
postorder(root)
