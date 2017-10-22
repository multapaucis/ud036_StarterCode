import webbrowser


class Movie():
    """Provides a way to store movie data and related information"""

    def __init__(self, movie_title, duration, movie_story, movie_poster,
                 movie_trailer):
        '''Constructs an instance of the Movie Class'''
        self.title = movie_title
        self.duration = duration
        self.storyline = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        '''Opens a trailer for the movie in the default browser'''
        webbrowser.open(self.trailer_youtube_url)
