import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Variables
quit = False

# Data Loading
original = pd.read_csv('Datasets/data/highest_hollywood_grossing_movies.csv')

# Data Cleaning
filter = original.drop(["Movie Info", "Domestic Opening (in $)", "Domestic Sales (in $)", "International Sales (in $)", "Release Date", "License"], axis = 1)

def clean_budget_column():
    def is_numeric(value):
        return bool(re.match(r'^\d+$', str(value)))
    filter['Budget (in $)'] = filter['Budget (in $)'].apply(lambda x: x if is_numeric(x) else 0)

clean_budget_column()
# Unfortunately, the creator of the dataset has added some wrong inputs into the 'Budget' column of the dataset.
# This has prevented me from adding options in the User Interface relating to budgets.
# This also means that goal 2 cannot be fulfilled.

# Dataframe Test
filter.head()

# Data Analysis
# The worldwide box office
def total_sales():
   totl_sales = int(filter['Worldwide Sales (in $)'].sum())
   print(f"The total worldwide box office for all of the 1000 movies combined in USD is: ${totl_sales:,}")

def avg_sales():
   average_sales = int(filter['Worldwide Sales (in $)'].mean())
   print(f"The average worldwide box office for all of the 1000 movies combined in USD is: ${average_sales:,}")

def med_sales():
   median_sales = int(filter['Worldwide Sales (in $)'].median())
   print(f"The box office median in all of the 1000 movies in USD is: ${median_sales:,}")

def mod_sales():
   mode_sales = filter['Worldwide Sales (in $)'].mode()[0]
   print(f"The box office value that appeared the most in the dataset is: ${mode_sales:,}")

def min_box_office():
   min_index = filter['Worldwide Sales (in $)'].idxmin()
   min_movie = filter.loc[min_index, 'Title']
   min_sales = int(filter['Worldwide Sales (in $)'].min())
   min_year = filter.loc[min_index, 'Year']
   print(f"The movie that grossed the least in the dataset is {min_movie} ({min_year}), with a worldwide box office of ${min_sales:,}")

def max_box_office():
   max_index = filter['Worldwide Sales (in $)'].idxmax()
   max_movie = filter.loc[max_index, 'Title']
   max_sales = int(filter['Worldwide Sales (in $)'].max())
   max_year = filter.loc[max_index, 'Year']
   print(f"The movie that grossed the most in the dataset is {max_movie} ({max_year}), with a worldwide box office of ${max_sales:,}")

# The duration
def avg_duration():
    filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
    average_duration = filter['Running Time (in minutes)'].mean()
    print(f"The average running time for all 1000 movies is: {average_duration:.2f} minutes")

def total_duration():
    filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
    total_duration = filter['Running Time (in minutes)'].sum()
    print(f"The total running time for all 1000 movies is: {total_duration} minutes")

def med_duration():
    filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
    median_duration = filter['Running Time (in minutes)'].median()
    print(f"The median running time for all 1000 movies is: {median_duration} minutes")

def mod_duration():
   filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
   mode_duration = filter['Running Time (in minutes)'].mode()[0]
   print(f"The running time value that appeared the most in the dataset is: {mode_duration} minutes")

def min_duration():
   filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
   min_index = filter['Running Time (in minutes)'].idxmin()
   min_movie = filter.loc[min_index, 'Title']
   min_duration = int(filter['Running Time (in minutes)'].min())
   min_year = filter.loc[min_index, 'Year']
   print(f"The shortest movie in the dataset is {min_movie} ({min_year}), with a total of only {min_duration} minutes")

def max_duration():
   filter['Running Time (in minutes)'] = filter['Running Time'].apply(convert_to_minutes)
   max_index = filter['Running Time (in minutes)'].idxmax()
   max_movie = filter.loc[max_index, 'Title']
   max_duration = int(filter['Running Time (in minutes)'].max())
   max_year = filter.loc[max_index, 'Year']
   print(f"The longest movie in the dataset is {max_movie} ({max_year}), with a total of {max_duration} minutes")

# Function Definitions
def show_original():
    print(original)

def show_filter():
    print(filter)

def top_20_movies():
    top_movies = filter.sort_values(by = 'Worldwide Sales (in $)', ascending = False).head(20)
    for i, (index, row) in enumerate(top_movies.iterrows(), start = 1):
        print(f"{i}. {row['Title']} - ${int(row['Worldwide Sales (in $)']):,}")

def bottom_20_movies():
    bottom_movies = filter.sort_values(by = 'Worldwide Sales (in $)', ascending = True).head(20)
    for i, (index, row) in enumerate(bottom_movies.iterrows(), start = 1):
        print(f"{i}. {row['Title']} - ${int(row['Worldwide Sales (in $)']):,}")

def most_common_genre():
    genre_counter = Counter()
    for genres in filter['Genre']:
        genre_list = eval(genres)
        genre_counter.update(genre_list)
    most_popular_genre = genre_counter.most_common(1)[0]
    print(f"The most common genre is '{most_popular_genre[0]}', with a total of {most_popular_genre[1]} movies in the dataset!")

def least_common_genre():
    genre_counter = Counter()
    for genres in filter['Genre']:
        genre_list = eval(genres)
        genre_counter.update(genre_list)
    least_popular_genre = genre_counter.most_common()[-1]
    print(f"The least common genre is '{least_popular_genre[0]}', with a total of {least_popular_genre[1]} movie/s in the dataset!")

def most_common_year():
    year_counter = Counter(filter['Year'])
    most_popular_year = year_counter.most_common(1)[0]
    print(f"The year that released the most popular Hollywood movies is {most_popular_year[0]}, with {most_popular_year[1]} movies in the dataset released that year!")

def least_common_year():
    year_counter = Counter(filter['Year'])
    least_popular_year = year_counter.most_common()[-1]
    print(f"The year that released the least popular Hollywood movies is {least_popular_year[0]}, with {least_popular_year[1]} movie/s in the dataset released that year!")

def convert_to_minutes(running_time):
    try:
        hours = re.search(r'(\d+) h', running_time)
        minutes = re.search(r'(\d+) m', running_time)
        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        total_minutes = hours * 60 + minutes
        return total_minutes
    except Exception as e:
        print(f"Error processing '{running_time}': {e}")
        return 0

def max_distributor():
    filter['Distributor'] = filter['Distributor'].astype(str)
    exploded_df = filter.explode('Distributor')
    exploded_df['Distributor'] = exploded_df['Distributor'].str.strip()
    distributor_counts = exploded_df['Distributor'].value_counts()
    most_distributed_distributor = distributor_counts.idxmax()
    most_distributed_count = distributor_counts.max()
    print(f'The distributor that distributed the most movies in the dataset is {most_distributed_distributor}, who distributed a total of {most_distributed_count} movies in the dataset.')

def min_distributor():
    filter['Distributor'] = filter['Distributor'].astype(str)
    exploded_df = filter.explode('Distributor')
    exploded_df['Distributor'] = exploded_df['Distributor'].str.strip()
    distributor_counts = exploded_df['Distributor'].value_counts()
    least_distributed_distributor = distributor_counts.idxmin()
    least_distributed_count = distributor_counts.min()
    print(f'The distributor that distributed the least movies in the dataset is {least_distributed_distributor}, who distributed a total of {least_distributed_count} movie/s in the dataset.')

# Visualizing the data with Matplotlib
def show_charts():
    filter.plot(
                kind='scatter',
                x='Title',
                y='Worldwide Sales (in $)',
                color='blue',
                alpha=0.3,
                fontsize=1,
                title='Worldwide Sales of Movies in USD')
    plt.show()

# Data Reporting        
filter.to_csv("Datasets/data/highest_hollywood_grossing_movies_updated.csv", index = False)

# The User Interface
def UI():
    global quit

    print("""Welcome to the Dataset Visualization!\nNote: The information only comes from the data included in the dataset, so the lowest grossing movie shown in this list is not actually the lowest grossing movie in the world, but rather\nthe lowest grossing movie in the dataset.\n       
    Please select an option:
    1 - Show the original dataset
    2 - Show the cleaned dataframe
    3 - Visualise the worldwide sales of movies in USD
    4 - Show the total worldwide box office for all of the movies combined in USD
    5 - Show the average worldwide box office for all of the movies in USD
    6 - Show the box office median in all of the movies in USD
    7 - Show the box office value that appeared the most in the dataset
    8 - Show the movie that grossed the most in the dataset
    9 - Show the movie that grossed the least in the dataset
    10 - Show the total duration for all of the movies combined in the dataset
    11 - Show the average duration for all of the movies in USD
    12 - Show the duration median in all of the movies in USD
    13 - Show the duration value that appeared the most in the dataset
    14 - Show the longest movie in the dataset
    15 - Show the shortest movie in the dataset
    16 - Show the top 20 highest grossing movies in the dataset
    17 - Show the bottom 20 lowest grossing movies in the dataset
    18 - Show the most common genre for all of the movies
    19 - Show the least common genre for all of the movies
    20 - Show the year that released the most movies from the dataset
    21 - Show the year that released the least movies from the dataset
    22 - Show the distributor that distributed the most movies from the dataset
    23 - Show the distributor that distributed the least movies from the dataset
    24 - Exit
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
            total_sales()
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
            total_duration()
        elif choice == 11:
            avg_duration()
        elif choice == 12:
            med_duration()
        elif choice == 13:
            mod_duration()
        elif choice == 14:
            max_duration()
        elif choice == 15:
            min_duration()
        elif choice == 16:
            top_20_movies()
        elif choice == 17:
            bottom_20_movies()
        elif choice == 18:
            most_common_genre()
        elif choice == 19:
            least_common_genre()
        elif choice == 20:
            most_common_year()
        elif choice == 21:
            least_common_year()
        elif choice == 22:
            max_distributor()
        elif choice == 23: 
            min_distributor()
        elif choice == 24:
            quit = True
        else:
            print('Not a valid number')

    except:
        print("Something went wrong! This could either be your fault (not typing in a number) or my fault (a bug). But whoever's fault this is, I apologize for the inconvenience. Perhaps just try again?")

# Main program
while not quit:
    UI()