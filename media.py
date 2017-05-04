import webbrowser

class Movie():
    """Summary of class here.

       Attributes:
       movie_title: A string contains the tile of movie
       movie_storyline: A string contains the storyline of movie
       poster_image: A string contains the url link of movie poster
       trailer_youtube: A string contains the url link of movie trailer
       release_date: A string contains the release date of moive

       Methods:
       show_trailer(): open a youtube link of movie trailer in web browser
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
