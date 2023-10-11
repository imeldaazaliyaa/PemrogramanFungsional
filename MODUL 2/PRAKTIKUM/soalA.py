class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    borrow_book = lambda self, book: (
        (lambda: print(f"{self.name} meminjam buku: {book.title} oleh {book.author}"))
        if book.is_available
        else (lambda: print(f"Buku {book.title} sedang dipinjam oleh orang lain."))
    )

    return_book = lambda self, book: (
        (lambda: print(f"{self.name} mengembalikan buku: {book.title} oleh {book.author}"))
        if book in self.borrowed_books
        else (lambda: print(f"{self.name} tidak memiliki buku ini."))
    )

class Admin:
    def __init__(self, name):
        self.name = name

    add_book = lambda self, library, title, author: (
        (lambda: library.append(Book(title, author)))
        and (lambda: print(f"{self.name} menambahkan buku baru: {title} oleh {author}"))
    )

    find_book = lambda self, library, title: [book for book in library if book.title == title]

    edit_book = lambda self, library, title, new_title, new_author: (
        (lambda: [
            setattr(book, "title", new_title),
            setattr(book, "author", new_author)
        ])
        for book in self.find_book(library, title)
    )

def main():
    library = []
    admin = Admin("Admin1")
    user1 = User("User1")
    user2 = User("User2")

    while True:
        print("\nPilihan:")
        print("1. Tambah Buku (Admin)")
        print("2. Pinjam Buku (User)")
        print("3. Kembalikan Buku (User)")
        print("4. Temukan Buku (Admin)")
        print("5. Edit Buku (Admin)")
        print("6. Keluar")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama penulis: ")
            admin.add_book(library, title, author)
        elif choice == "2":
            user = input("Masukkan nama pengguna: ")
            book_title = input("Masukkan judul buku yang ingin dipinjam: ")
            books_to_borrow = admin.find_book(library, book_title)
            if books_to_borrow:
                user1.borrow_book(books_to_borrow[0])
            else:
                print(f"Buku {book_title} tidak ditemukan.")
        elif choice == "3":
            user = input("Masukkan nama pengguna: ")
            book_title = input("Masukkan judul buku yang ingin dikembalikan: ")
            books_to_return = admin.find_book(library, book_title)
            if books_to_return:
                user1.return_book(books_to_return[0])
            else:
                print(f"Buku {book_title} tidak ditemukan.")
        elif choice == "4":
            title = input("Masukkan judul buku yang ingin ditemukan: ")
            found_books = admin.find_book(library, title)
            if found_books:
                print(f"Buku ditemukan: {', '.join([book.title for book in found_books])}")
            else:
                print(f"Buku {title} tidak ditemukan.")
        elif choice == "5":
            title = input("Masukkan judul buku yang ingin diedit: ")
            new_title = input("Masukkan judul baru: ")
            new_author = input("Masukkan penulis baru: ")
            admin.edit_book(library, title, new_title, new_author)
        elif choice == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
