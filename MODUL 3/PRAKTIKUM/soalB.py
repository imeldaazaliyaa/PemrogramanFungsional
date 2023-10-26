from functools import reduce

# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Pilihan fungsi
def jumlah_film_berdasarkan_genre(movies):
    genre_counts = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
    return genre_counts

def rata_rata_rating_film_berdasarkan_tahun(movies):
    rating_by_year = {}
    count_by_year = {}
    for movie in movies:
        year = movie["year"]
        rating = movie["rating"]
        if year in rating_by_year:
            rating_by_year[year] += rating
            count_by_year[year] += 1
        else:
            rating_by_year[year] = rating
            count_by_year[year] = 1
    avg_rating_by_year = {year: rating / count for year, rating, count in zip(rating_by_year.keys(), rating_by_year.values(), count_by_year.values())}
    return avg_rating_by_year

def film_dengan_rating_tertinggi(movies):
    highest_rated_movie = max(movies, key=lambda x: x["rating"])
    return highest_rated_movie

def tampilkan_info_film(movie):
    return f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Genre: {movie['genre']}"

while True:
    print("\nPilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if choice == '1':
        genre_counts = jumlah_film_berdasarkan_genre(movies)
        print("Jumlah Film Berdasarkan Genre:")
        print(genre_counts)
    elif choice == '2':
        avg_rating_by_year = rata_rata_rating_film_berdasarkan_tahun(movies)
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        for year, avg_rating in avg_rating_by_year.items():
            print(f"Tahun {year}: {avg_rating:.2f}")
    elif choice == '3':
        highest_rated_movie = film_dengan_rating_tertinggi(movies)
        print("Film dengan Rating Tertinggi:")
        print(tampilkan_info_film(highest_rated_movie))
    elif choice == '4':
        title = input("Masukkan judul film: ")
        movie = next((movie for movie in movies if movie["title"] == title), None)
        if movie:
            print(tampilkan_info_film(movie))
        else:
            print("Film tidak ditemukan.")
    elif choice == '5':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor tugas yang sesuai.")
