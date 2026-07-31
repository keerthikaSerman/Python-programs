class stack:
    def __init__(self):
        self.stack = []
        

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if self.is_empty():
            print("No Book in the Stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("No Book in the Stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    def display(self):
        print("Books in the Stack :", self.stack)

book=stack()
book.push("You Can")
book.push("The art of being Alone")
book.push("The art of laszness")
print("What is your query?")
print("1.Adding Book name")
print("2.Deleting Book name")
print("3.Checking the Book in the Top")
print("4.Check the number of books in the Stack")
choice=int(input("Enter your option:"))
if choice==1:
    n=int(input("Enter number of books to add:"))
    for i in range(n):
        item=input("Enter Book name:")
        book.push(item)
elif choice==2:        
    print("Deleted book is:",book.pop())
    book.display()
elif choice==3:
    print("The Top Book in the stack:",book.peek())
elif choice==4:
    print("Number of book in the Stack:",book.size())
    book.display()
else:
    print("Invalid Choice")
    
        

