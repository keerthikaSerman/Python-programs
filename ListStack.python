class Node:
    def __init__(self, data):
        self.data = "data"
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        print("The Stack is empty")

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} added successfully")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
        return self.top.data
    
        
        
book = Stack()
print("What is query?")
print("1.Add book to Stack")
print("2.Deleting Book name")
print("3.Checking the Book in the Top")
print("4.Check the number of books in the Stack")
choice=int(input("Enter your choice"))
if choice==1:
    n=int(input("Enter number of books to add:"))
    for i in range(n):
        item=input("Enter Book name:")
        book.push(item)
    
elif choice==2:        
    book.pop()
    book.display()
elif choice==3:
    print("The Top Book in the stack:",book.peek())
elif choice==4:
    print("Number of book in the Stack:",book.size())
else:
    print("Invalid Choice")
    
