

def fav_movies():
    kids_fav_movies = {
                        'Johnson' : 'The Dark Knight',
                        'Harris'  : 'Lord of Rings',
                        'Steve'   : 'Titanic'
                        }
    print(kids_fav_movies)
    if 'steve' in kids_fav_movies:
        del kids_fav_movies['steve']
    if 'Steve' in kids_fav_movies:
        kids_fav_movies.pop('Steve')
    print(kids_fav_movies)

if __name__ == '__main__':
    fav_movies()