import webbrowser
# Class template for our Movies listing. Contains the __init__ and a custom definition to show the trailer on click.
class Movie():
    """General information of the movies we use."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # These are our instance common attributes, we pass the Title, Storyline, image and youtube trailer link.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, review_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = review_rating

    # Opens WebBrowser and plays the Youtube trailer specified.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
