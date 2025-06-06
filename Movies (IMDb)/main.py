# Modules
import pandas as pd
import matplotlib.pyplot as plt

# Global Variables
quit = False

# Loading the datasets
df_original = pd.read_csv('Movies (IMDb)/data/imdb_top_1000.csv')

# Update and remove the unecessary columns (remove spaces from column title, so it works)
df_original.columns = df_original.columns.str.strip() 

# Update the dataframe
df_updated = df_original.drop(['Poster_Link', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes', 'Gross'], axis=1,)
df_updated.to_csv('Movies (IMDb)/data/imdb_top_1000_updated.csv')

# Functions
def showData():
    print("Here is the original dataset.")
    print(df_original) # I don't think you need an explanation for this one...

def updatedData():
    print("Here is the updated dataset.")
    print(df_updated) # Same for this lol

def visualizeHistogram():
    df_original['IMDB_Rating'].hist(
        bins=10, 
        color='blue', 
        alpha=0.3,
        )
    
    plt.title('Distribution of IMDb Ratings')
    plt.xlabel('IMDb Rating')
    plt.ylabel('Frequency')
    plt.show() # Makes a histogram on the ratings of movies

def showColumn():
       column_name = (input("""
                      
        Please choose a column from the following:
    [1] Poster_Link (most may not work due to dataframe being outdated)
    [2] Series_Title
    [3] Released_Year
    [4] Certificate
    [5] Runtime
    [6] Genre
    [7] IMDB_Rating
    [8] Overview
    [9] Meta_score
    [10] Director, Star1, Star2, Star3, Star4
    [15] No_of_votes
    [16] Gross
                      
    Enter column name: """))
       if column_name in df_original.columns:
        if column_name == 'Series_Title':
            combined_df = df_original[['Series_Title']] # If they just enter Series_Title then it just shows that instead of two options.
        else:
            combined_df = df_original[['Series_Title', column_name]]

        print(f"Showing {column_name}:")
        print(combined_df) # Adds the Series_Title and the user input in 1 dataset.

def top50Movies():
    topmovies = df_original.sort_values(by='No_of_Votes', ascending=False).head(50)
    topmovies = topmovies.drop(['Poster_Link', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'Overview', 'Meta_score', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'Gross'], axis=1)
    print("Here are the top 50 movies in the dataset:")
    print(topmovies) # Sorts the movies in order and drops the useless columns

def bottom50Movies():
    bottommovies = df_original.sort_values(by='No_of_Votes', ascending=True).head(50) 
    bottommovies = bottommovies.drop(['Poster_Link', 'Released_Year', 'Certificate', 'Runtime', 'Genre', 'Overview', 'Meta_score', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'Gross'], axis=1)
    print("Here are the bottom 50 movies in the dataset:")
    print(bottommovies) # Same as top20Movies(), but for ascending order

def findMoviesByYear():
    year_to_find = int(input("Enter a year to sort the movies: "))
    df_original['Released_Year'] = pd.to_numeric(df_original['Released_Year'], errors='coerce') # Converts data to numeric

    matching_years = df_original[df_original['Released_Year'] == year_to_find]
        
    if matching_years.empty:
        print(f"No movies found for the year {year_to_find}.")

    else:
        print(f"Here are the movies in the year {year_to_find}:")
        print(matching_years[['Series_Title', 'Released_Year', 'IMDB_Rating']])
        # Finds the year and lists all the movies in it

def findMoviesByGenre():
    genre_to_find = input("""
                          
        Please enter a genre:
    [1] Action
    [2] Adventure
    [3] Animation
    [4] Biography
    [5] Comedy
    [6] Crime
    [7] Drama
    [8] Family
    [9] Fantasy
    [10] Film-Noir
    [11] History
    [12] Horror
    [13] Music
    [14] Musical
    [15] Mystery
    [16] Romance
    [17] Sci-Fi
    [18] Sport
    [19] Thriller
    [20] War
    [21] Western
                               
    Enter a genre: """)

    matching_movies = []

    for index, row in df_original.iterrows():
        genres = [genre.strip() for genre in row['Genre'].split(',')]
        if genre_to_find in genres:
            matching_movies.append(row)

    matching_movies_df = pd.DataFrame(matching_movies)

    if matching_movies_df.empty:
        print(f"The genre \"{genre_to_find}\" has not been found. Did you misspell something?")

    else:
        print(f"Movies with the genre \"{genre_to_find}\":")
        print(matching_movies_df[['Series_Title', 'Genre']]) # Prints the movies with the user's genre and the movie name

def averageRuntime():
    df_original['Runtime'] = df_original['Runtime'].str.replace(' min', '').astype(float)
    avg_runtime = df_original['Runtime'].mean()
    print(f"The average runtime of movies is {avg_runtime} minutes.") # Finds mean of all movies

def mainUI():
    global quit

    print("""

        Welcome to the IMDb dataset program! Please use numbers to navigate the following options:
    [1] -> Show the original dataset
    [2] -> Show the updated dataset
    [3] -> Visualise distributed IMDb ratings in a histogram
    [4] -> View a specific column
    [5] -> View the top 50 most popular movies (sorted by No_of_Votes)
    [6] -> View the 50 least popular movies in the dataset (sorted by No_of_Votes)
    [7] -> Sort by Released_Year
    [8] -> Sort by Genre
    [9] -> Find the average runtime of all the movies combined
    [10] -> Quit
     
    """)

    try:
        answer = int(input('Enter input: '))

        if answer == 1:
            showData()
        elif answer == 2:
            updatedData()
        elif answer == 3:
            visualizeHistogram()
        elif answer == 4:
            showColumn()
        elif answer == 5:
            top50Movies()
        elif answer == 6:
            bottom50Movies()
        elif answer == 7:
            findMoviesByYear()
        elif answer == 8:
            findMoviesByGenre()
        elif answer == 9:
            averageRuntime()
        elif answer == 10:
            quit = True
            print('Thank you for using this UI. Goodbye! - Alex')
        else:
            print('Incorrect syntax. Please enter a number between 1 and 10.')

    except ValueError:
        print('Invalid syntax, enter a number.')

# Main Program
while not quit:
    mainUI()