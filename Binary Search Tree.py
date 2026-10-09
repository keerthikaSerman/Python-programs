
    def _inorder(self, root, res):
        if root:
            self._inorder(root.left, res)
            res.append((root.id, root.name, root.course))
            self._inorder(root.right, res)

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res
   

    def _count(self, root):
        return 1 + self._count(root.left) + self._count(root.right) if root else 0

    def count(self):
        return self._count(self.root)

    def display(self, node=None, lvl=0, p="Root: "):
        if lvl == 0: node = self.root
        if not node: print("[Database is empty]"); return
        print("    " * lvl + p + f"[ID: {node.id} | Name: {node.name} | Course: {node.course}]")
        if node.left: self.display(node.left, lvl + 1, "L--- ")
        if node.right: self.display(node.right, lvl + 1, "R--- ")


tree = AVLTree()
while True:
    print("\n--- MENU ---")
    print("1. Insert  2. Delete  3. Search  4. Sort (In-order)  5. Count  6. Exit")
    ch = input("Enter choice: ").strip()
   
    if ch == '1':
        try:
            tree.insert(int(input("ID: ")), input("Name: "), input("Course: "))
            print("\n[Updated Tree Structure After Insertion]:")
            tree.display()
        except ValueError:
            print("Invalid ID format. Must be an integer.")
    elif ch == '2':
        try:
            tree.delete(int(input("ID to delete: ")))
            print("\n[Updated Tree Structure After Deletion]:")
            tree.display()
        except ValueError:
            print("Invalid ID format. Must be an integer.")
    elif ch == '3':
        try:
            r = tree.search(int(input("ID to search: ")))
            print(f"\n[Search Result] -> ID: {r.id}, Name: {r.name}, Course: {r.course}" if r else "\n[Search Result] -> Not found.")
        except ValueError:
            print("Invalid ID format.")
    elif ch == '4':
        print("\n[Sorted Enrollments by ID]:")
        records = tree.inorder()
        for rec in records:
            print(f"ID: {rec[0]} | Name: {rec[1]} | Course: {rec[2]}")
        if not records: print("[Database is empty]")
    elif ch == '5':
        print(f"\n[Total Enrollments]: {tree.count()}")
    elif ch == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
