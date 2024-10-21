#task1
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    new_book = (title, author)
    
    if new_book not in library:
        library.append(new_book)
        print(f'Added "{title}" by {author} to the library.')
    else:
        print(f'"{title}" by {author} is already in the library.')


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library)

print(library)
#task2 I don't know if the question is asking to allow input or not so I will do it both ways.
def add_book2(library2, new_book2):
    if new_book2 not in library2:
        library2.append(new_book2)
    else:
        print("This book is already in the library.")

library2 = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book2(library2, ("Lasagna", "Pizza"))
add_book2(library2, ("1984", "George Orwell"))

print(library2)