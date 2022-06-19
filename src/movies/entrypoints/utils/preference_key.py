import math

## SINGLE RESPONSIBILITY PRINCIPLE ##
def key(genres):
    genres_list = genres.split(',')
    key = [1 if genre == 'Comedy' 
            else 2 if genre == 'Drama' 
            else 3 if genre == 'Sci-Fi'
            else 4 if genre == 'Romantic'
            else 5 if genre == 'Adventure' else 0 for genre in genres_list]
    return math.prod(key) % 5 + 1