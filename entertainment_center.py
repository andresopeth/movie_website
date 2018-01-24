import media
import fresh_tomatoes

world_of_warcraft = media.Movie("World of Warcraft", "The fight to survive between two races.", "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Warcraft_Teaser_Poster.jpg/220px-Warcraft_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=2Rxoz13Bthc", "6.9")

matrix = media.Movie("Matrix", "A simulated reality and the fight to escape from it.", "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=m8e-FF8MsqU", "8.7")

lotr = media.Movie("Lord of The Rings", "A group of adventurers on a quest.", "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=F4J9-CQXdPk&", "8.8")

the_hobbit = media.Movie("The Hobbit", "A group of adventurers on a quest through middle earth.", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/The_Hobbit_trilogy_dvd_cover.jpg/220px-The_Hobbit_trilogy_dvd_cover.jpg", "https://www.youtube.com/watch?v=SDnYMbYB-nU", "7.9")

interstellar = media.Movie("Interstellar", "Humanity struggle to survive and a trip to the unknown.", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E", "8.6")

sphere = media.Movie("Sphere", "The discovery of a spaceship.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyMTBlM2UtNWE1Ni00ZDg4LTliODQtYTFhZWIwNTAyNTg3L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=kozds_anirw", "6.1")

movies = [world_of_warcraft, matrix, lotr, the_hobbit, interstellar, sphere]
fresh_tomatoes.open_movies_page(movies)
