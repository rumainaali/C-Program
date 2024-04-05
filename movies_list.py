#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like



first_friend_movies = []

while True:
    movie = input("Friend 1: \nWhat movies do you like? (Enter 'completed' when done) ").strip().lower()
    if movie == 'completed':
        break
    first_friend_movies.append(movie)

commonMovieCount = 0

while commonMovieCount < 3:
    second_friend_movies = []
    while True:
        movie = input("Second friend: \n What movies do you like? (Enter 'completed' when done) ").strip().lower()
        if movie == 'completed':
            break
        
        if movie in first_friend_movies:
            print("You both like", movie)
            commonMovieCount += 1
        second_friend_movies.append(movie)