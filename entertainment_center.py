import media
import fresh_tomatoes

""" Create instances using class Movie and group all instances in a list"""

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "1995")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
    "2009")

your_name = media.Movie(
    "Your Name",
    "A story of a high school girl in rural Japan and a high school boy "
    "in Tokyo who swap bodies",
    "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
    "https://www.youtube.com/watch?v=dbtN9HOOqhk",
    "2016")

ghost_in_shell = media.Movie(
    "Ghost in Shell",
    "A story of the plot follows the Major, a cyborg supersoldier who "
    "yearns to learn her past",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/Ghost_in_the_Shell"
    "_%282017_film%29.png/220px-Ghost_in_the_Shell_%282017_film%29.png",
    "https://www.youtube.com/watch?v=G4VmJcZR0Yg",
    "2017")

fifty_shades_of_grey = media.Movie(
    "Fifty Shades of Grey",
    "A story of a college graduate who begins a sadomasochistic relationship "
    "with young business magnate Christian Grey",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Fifty-Gray-poster."
    "jpg/220px-Fifty-Gray-poster.jpg",
    "https://www.youtube.com/watch?v=SfZWFDs0LxA",
    "2015")

fullmetal_alchemist = media.Movie(
    "Fullmetal Alchemist",
    "A Japanese science fantasy action adventure film based on the manga "
    "series of the same name by Hiromu Arakawa",
    "http://d32qys9a6wm9no.cloudfront.net/images/movies/poster/73/"
    "da476c90fb59650a14f0d193be161cad_500x735.jpg?t=1492009668",
    "https://www.youtube.com/watch?v=j3xvctz7l1M",
    "2017")
movies = [toy_story,
          avatar, your_name,
          ghost_in_shell,
          fifty_shades_of_grey,
          fullmetal_alchemist]

""" Build HTML file and display movie website """
fresh_tomatoes.open_movies_page(movies)
