import fresh_tomatoes
import media

# Create movie instances
toy_story = media.Movie("Toy Story","https://www.youtube.com/watch?v=KYz2wyBy3kc")
top_gun = media.Movie("Top Gun", "https://www.youtube.com/watch?v=qAfbp3YX9F0")
pretty_woman = media.Movie("Pretty Woman", "https://www.youtube.com/watch?v=Wzii8IuL8lk")

# List of movies to appear on the website
movies = [toy_story, top_gun, pretty_woman]

# Build Fresh Tomatoes Webpage
fresh_tomatoes.open_movies_page(movies)


