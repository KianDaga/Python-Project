movie1 = ("The Dark Night", 2008, "Action")
movie2 = ("Inception", 2010, "Sci-Fi")

movie_library = (movie1, movie2)

for movie in movie_library:
    if movie[1] >= 2010:
        print(movie[0])