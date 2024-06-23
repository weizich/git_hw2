library = {}

def add_book():
    """
    提示用戶輸入書名、類別和價格，並用垂直線分隔。
    將書籍添加到圖書館字典中，書名作為鍵，類別和價格作為值。
    """
    book_info = input("Enter the title, genre, and price of the book separated by vertical bars (|): ")
    try:
        title, genre, price = book_info.split('|')
        title, genre = title.strip(), genre.strip()
        price = float(price.strip())
        library[title] = (genre, price)
        print(f"Book '{title}' added to the library.")
        return True
    except ValueError:
        print("Invalid input format. Please enter the title, genre, and price separated by vertical bars.")
        return False

def remove_book():
    """
    提示用戶輸入要移除的書名。
    如果書名存在於圖書館中，則將其移除並打印提示信息。
    """
    title = input("Enter the title of the book you want to remove: ").strip()
    if title in library:
        del library[title]
        print(f"Book '{title}' has been removed from the library.")
        return True
    else:
        print(f"Book '{title}' not found in the library.")
        return False

def get_book_info():
    """
    提示用戶輸入要查詢的書名。
    如果書籍存在於圖書館中，則打印書名、類別和價格。
    """
    title = input("Enter the title of the book: ").strip()
    if title in library:
        genre, price = library[title]
        print(f"Title: {title}\nGenre: {genre}\nPrice: ${price:.2f}")
    else:
        print(f"Book '{title}' not found in the library.")

def list_books():
    """
    以字母順序列出圖書館中的所有書籍。
    如果圖書館是空的，則打印提示信息。
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print(f"{title} ({genre}, ${price:.2f})")
    print()
    return True

def list_books_by_genre():
    """
    提示用戶輸入要查詢的類別。
    以字母順序列出圖書館中指定類別的所有書籍。
    如果未找到相關書籍，則打印提示信息。
    """
    genre_search = input("Enter the genre: ").strip()
    found_books = {title: (genre, price) for title, (genre, price) in library.items() if genre.lower() == genre_search.lower()}
    
    if not found_books:
        print(f"No books found in the genre '{genre_search}'.")
        return False
    print()
    for title, (genre, price) in sorted(found_books.items()):
        print(f"{title} ({genre}, ${price:.2f})")
    print()
    return True

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")
