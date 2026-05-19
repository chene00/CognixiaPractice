movieList = {}

addMore = True

# Allow multiple movie inputs
while addMore:
    # Prompt user
    x = input("Enter movie name followed by the rating (1 - 5): ")
    
    # Parse user input
    movies = x.split(" ")

    # Extract the movie data
    movieName = movies[0]
    movieRating = int(movies[1])

    # Check if movie is already in the dictionary
    if movieName in movieList:
        # If so just add the new rating value
        movieList[movieName].append(movieRating)
    else:
        # Else create a new entry in the dictionary
        movieList[movieName] = [movieRating]

    # Prompt user to exit
    y = input("Exit and Show Results? (Y/N): ")

    # If user wants to exit, exit while loop
    if y.upper() == 'Y':
        addMore = False

# Create new empty dictionary
movieAverage = {}

# Caclulate the average of each movie and add it to the new dictionary
for _, (key, value) in enumerate(movieList.items()):
    movieAverage[key] = sum(value) / len(movieList[key])

# Print out the results
for movie, avg in movieAverage.items():
    print(f"{movie} : {avg}")
