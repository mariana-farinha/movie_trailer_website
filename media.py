import webbrowser
import urllib2
import urllib
import json

class Movie():
    def __init__(self, movie_title,trailer_youtube):
        params = {'t': movie_title} 
        url = "http://www.omdbapi.com/?" + urllib.urlencode(params)+"&y=&plot=short&r=json"
        try:
            response = urllib2.urlopen(url)
            body = response.read()
            body_json = json.loads(body)
            self.title = movie_title
            self.trailer_youtube_url = trailer_youtube
            self.storyline = body_json['Plot']
            self.actors = body_json['Actors']
            self.poster_image_url = body_json['Poster']
            self.rated = body_json['Rated']
            self.runtime = body_json['Runtime']
            self.year = body_json['Year']
            self.imdb_rating = body_json['imdbRating']
        except URLError, e:
            print 'Got an error code:', e

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
