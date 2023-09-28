class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} meminjam buku: {book.title} oleh {book.author}")
        else:
            print(f"Buku {book.title} sedang dipinjam oleh orang lain.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} mengembalikan buku: {book.title} oleh {book.author}")
        else:
            print(f"{self.name} tidak memiliki buku ini.")

class Admin:
    def __init__(self, name):
        self.name = name

    def add_book(self, library):
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama penulis: ")
        new_book = Book(title, author)
        library.append(new_book)
        print(f"{self.name} menambahkan buku baru: {title} oleh {author}")

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
        print("4. Keluar")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            admin.add_book(library)
        elif choice == "2":
            user = input("Masukkan nama pengguna: ")
            book_title = input("Masukkan judul buku yang ingin dipinjam: ")
            for book in library:
                if book.title == book_title:
                    user1.borrow_book(book)
        elif choice == "3":
            user = input("Masukkan nama pengguna: ")
            book_title = input("Masukkan judul buku yang ingin dikembalikan: ")
            for book in library:
                if book.title == book_title:
                    user1.return_book(book)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
