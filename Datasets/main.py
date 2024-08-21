import pandas as pd
import matplotlib.pyplot as plt

# -- Variables --
quit = False

# Data Loading
original = pd.read_csv('Datasets/data/highest_hollywood_grossing_movies.csv')

# Data Cleaning
filter = original.drop(["Movie Info", "Domestic Opening (in $)", "Domestic Sales (in $)", "International Sales (in $)", "Release Date", "License"], axis = 1)
filterdebug = filter.drop(["Unnamed: 0"], axis = 1) 

# "Original" is the original dataset
# "Filter" is the dataframe that has been cleaned, but there is an extra column named "Unnamed: 0" that somehow appeared in the .csv version of "Filter".
# To remove this extra column, "Filterdebug" is created. "Filterdebug" removes the extra column from "Filter".

# Dataframe Test
filterdebug.head()

#---- Function Definitions ----#
def show_original():
    print(original)

def show_filter():
    print(filterdebug)

# Visualizing the data with Matplotlib
def show_charts():
    filterdebug.plot(
                kind='scatter',
                x='Title',
                y='Worldwide Sales (in $)',
                color='blue',
                alpha=0.3,
                fontsize=1,
                title='Worldwide Sales of Movies in USD')
    plt.show()

# Data Analysis
def avg_sales():
   average_sales = int(filterdebug['Worldwide Sales (in $)'].mean())
   print(f"The average worldwide box office for all of the 1000 movies combined in USD is: ${average_sales:,}")

def med_sales():
   median_sales = int(filterdebug['Worldwide Sales (in $)'].median())
   print(f"The box office median in all of the 1000 movies in USD is: ${median_sales:,}")

def mod_sales():
   mode_sales = filterdebug['Worldwide Sales (in $)'].mode()[0]
   print(f"The box office value that appeared the most in the dataset is: ${mode_sales:,}")

def min_box_office():
   min_index = filterdebug['Worldwide Sales (in $)'].idxmin()
   min_movie = filterdebug.loc[min_index, 'Title']
   min_sales = int(filterdebug['Worldwide Sales (in $)'].min())
   min_year = filterdebug.loc[min_index, 'Year']
   print(f"The movie that grossed the least in the dataset is {min_movie} ({min_year}), with a worldwide box office of ${min_sales:,}")

def max_box_office():
   max_index = filterdebug['Worldwide Sales (in $)'].idxmax()
   max_movie = filterdebug.loc[max_index, 'Title']
   max_sales = int(filterdebug['Worldwide Sales (in $)'].max())
   max_year = filterdebug.loc[max_index, 'Year']
   print(f"The movie that grossed the most in the dataset is {max_movie} ({max_year}), with a worldwide box office of ${max_sales:,}")

# Options
def top_20_movies():
    top_movies = filterdebug.sort_values(by = 'Worldwide Sales (in $)', ascending = False).head(20)
    for index, row in top_movies.iterrows():
        print(f"{row['Title']} - ${int(row['Worldwide Sales (in $)']):,}")

def bottom_20_movies():
    bottom_movies = filterdebug.sort_values(by = 'Worldwide Sales (in $)', ascending = True).head(20)
    for index, row in bottom_movies.iterrows():
        print(f"{row['Title']} - ${int(row['Worldwide Sales (in $)']):,}")

# Data Reporting        
filterdebug.to_csv("Datasets/data/highest_hollywood_grossing_movies_updated.csv")

# The User Interface
def UI():
    global quit

    print("""Welcome to the Dataset Visualization!\nNote: The information only comes from the data included in the dataset, so the lowest grossing movie shown in this list is not actually the lowest grossing movie in the world, but rather\nthe lowest grossing movie in the dataset.\n       
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated dataframe
    3 - Visualise the worldwide sales of movies in USD
    4 - Quit Program
    5 - Show the average worldwide box office for all of the movies combined in USD
    6 - Show the box office median in all of the 1000 movies in USD
    7 - Show the box office value that appeared the most in the dataset
    8 - Show the movie that grossed the most in the dataset
    9 - Show the movie that grossed the least in the dataset
    10 - Show the top 20 highest grossing movies in the dataset
    11 - Show the top 20 lowest grossing movies in the dataset
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            show_original()
        elif choice == 2:
            show_filter()
        elif choice == 3:
            show_charts()
        elif choice == 4:
            quit = True
        elif choice == 5:
            avg_sales()
        elif choice == 6:
            med_sales()
        elif choice == 7:
            mod_sales()
        elif choice == 8:
            max_box_office()
        elif choice == 9:
            min_box_office()
        elif choice == 10:
            top_20_movies()
        elif choice == 11:
            bottom_20_movies()
        else:
            print('Not a valid number')

    except:
        print("Something went wrong! This could either be your fault (not typing in a number) or my fault (a bug). But whoever's fault this is, I apologize for the inconvenience. Perhaps just try again?")

# Main program
while not quit:
    UI()