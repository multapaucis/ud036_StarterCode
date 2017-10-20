import media, fresh_tomatoes

toy_story = media.Movie("Toy Story",
	90,
	"What if Toys had Feelings?",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

mr_smith = media.Movie("Mr. Smith Goes To Washintgton",
	120,
	"What if Politicians had Morals?",
	"https://upload.wikimedia.org/wikipedia/en/c/ce/Smith_goes.jpg",
	"https://www.youtube.com/watch?v=qu2fDeRa1Jg")

jaws = media.Movie("Jaws",
	135,
	"What if Sharks were even Scarier?",
	"https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
	"https://www.youtube.com/watch?v=U1fu_sA7XhE")

skyfall = media.Movie("Skyfall",
	150,
	"'Member James Bond Movies?",
	"http://3.bp.blogspot.com/-QmPakkvmrQU/UOpD4fSjRVI/AAAAAAAACSY/RJfKNF-SS0o/s1600/Skyfall+Poster.jpg",
	"https://www.youtube.com/watch?v=6kw1UVovByw")

dalmatians = media.Movie("101 Dalmatians",
	85,
	"Puppies!",
	"https://i.jeded.com/i/101-dalmatians-one-hundred-and-one-dalmatians.25714.jpg",
	"https://www.youtube.com/watch?v=x4Nkw59KFBw"
	)

beauty= media.Movie("American Beauty",
	100,
	"Plastic Bag Blowing in the Breeze and Filler",
	"https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
	"https://www.youtube.com/watch?v=FfWnZthD9Tw")

movies = [toy_story, mr_smith, jaws, skyfall, dalmatians, beauty]
fresh_tomatoes.open_movies_page(movies)


